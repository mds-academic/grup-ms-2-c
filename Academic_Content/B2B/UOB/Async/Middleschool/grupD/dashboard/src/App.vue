<script setup>
import { ref, computed, onMounted, onUnmounted, watch, nextTick, reactive } from 'vue';
import { courseData } from './courseData.js';
import { getProject, types } from '@theatre/core';

const theatreState = {
  "revisionHistory": [],
  "definitionVersion": "0.4.0",
  "sheetsById": {
    "QuizSheet": {
      "sequence": {
        "type": "PositionalSequence",
        "length": 1,
        "tracksByObject": {
          "QuizOverlay": {
            "trackDataByPropertyPath": {
              "y": {
                "type": "BasicKeyframedTrack",
                "keyframes": [
                  { "id": "k1", "position": 0, "value": 80, "connectedRight": true, "handles": [ 0.5, 1, 0.5, 0 ] },
                  { "id": "k1b", "position": 0.3, "value": -15, "connectedRight": true, "handles": [ 0.5, 1, 0.5, 0 ] },
                  { "id": "k2", "position": 0.45, "value": 0, "connectedRight": true, "handles": [ 0.5, 1, 0.5, 0 ] }
                ]
              },
              "opacity": {
                "type": "BasicKeyframedTrack",
                "keyframes": [
                  { "id": "k3", "position": 0, "value": 0, "connectedRight": true, "handles": [ 0.5, 1, 0.5, 0 ] },
                  { "id": "k4", "position": 0.25, "value": 1, "connectedRight": true, "handles": [ 0.5, 1, 0.5, 0 ] }
                ]
              },
              "scale": {
                "type": "BasicKeyframedTrack",
                "keyframes": [
                  { "id": "k5", "position": 0, "value": 0.8, "connectedRight": true, "handles": [ 0.5, 1, 0.5, 0 ] },
                  { "id": "k5b", "position": 0.3, "value": 1.05, "connectedRight": true, "handles": [ 0.5, 1, 0.5, 0 ] },
                  { "id": "k6", "position": 0.45, "value": 1, "connectedRight": true, "handles": [ 0.5, 1, 0.5, 0 ] }
                ]
              }
            }
          }
        }
      }
    }
  }
};
const proj = getProject('LMSProject', { state: theatreState });
const sheet = proj.sheet('QuizSheet');
const quizObj = sheet.object('QuizOverlay', { y: 50, opacity: 0, scale: 0.95 });
const quizModalStyles = ref({ transform: 'translateY(50px) scale(0.95)', opacity: 0, display: 'none' });


// Reactive App States
const currentStep = ref(1);
const totalSteps = Object.keys(courseData).length;
const APP_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbz58EffczfpcNL0bvbD6VZvrY3mrVNtmpWasSwJT0baOowD2yGu_KNM0YNul9EtxxKVpg/exec';
const isLoggedIn = ref(false);
const loginSchool = ref('');
const loginEmail = ref('');
const selectedSchool = ref('');
const isLoggingIn = ref(false);
const showLoginError = ref(false);
const loginErrorTitle = ref('');
const loginErrorMessage = ref('');
const dashboardNotice = reactive({
  isOpen: false,
  type: 'warning',
  title: '',
  message: '',
  actionLabel: 'Mengerti',
  actionStep: null
});
const dashboardNoticeIcon = computed(() => ({
  success: 'OK',
  warning: '!',
  error: '!'
})[dashboardNotice.type] || '!');
const showDashboardNotice = ({ type = 'warning', title = 'Perhatian', message = '', actionLabel = 'Mengerti', actionStep = null } = {}) => {
  dashboardNotice.type = type;
  dashboardNotice.title = title;
  dashboardNotice.message = message;
  dashboardNotice.actionLabel = actionLabel;
  dashboardNotice.actionStep = actionStep;
  dashboardNotice.isOpen = true;
};
const closeDashboardNotice = () => {
  dashboardNotice.isOpen = false;
};
const handleDashboardNoticeAction = () => {
  if (dashboardNotice.actionStep) {
    currentStep.value = dashboardNotice.actionStep;
  }
  closeDashboardNotice();
};
const schoolOptions = ref([]);
const isSchoolLoading = ref(false);
const isSchoolDropdownOpen = ref(false);
const loginEmailAttempts = ref(0);
const loginEmailSuggestion = ref(null);
const emailHelpOpen = ref(false);
const emailHelpQuery = ref('');
const emailHelpResults = ref([]);
const isEmailHelpLoading = ref(false);

const showProfileMenu = ref(false);

const isDesktop = ref(window.innerWidth > 1024);
const updateWidth = () => { isDesktop.value = window.innerWidth > 1024; };
let schoolSearchTimer = null;
let schoolSearchRequestId = 0;

const studentData = ref({ name: '', school: '', email: '' });
const studentProgress = ref({}); // Menyimpan progress jawaban & attempts

// Tambahkan auto-ID ke semua soal agar gampang ditrack
Object.keys(courseData).forEach(stepId => {
  let qCounter = 1;
  courseData[stepId].quizzes?.forEach(quiz => {
    quiz.questions.forEach(q => {
      q.qid = `V${stepId}_Q${qCounter}`;
      qCounter++;
    });
  });
});

const saveProgress = (key, value) => {
  studentProgress.value[key] = value;
  localStorage.setItem('mds_student_progress', JSON.stringify(studentProgress.value));
  syncToSheets();
};

const markQuestionFailed = (qid) => {
  if (!qid) return;
  studentProgress.value[`${qid}_Ans`] = '0';
  studentProgress.value[`${qid}_Score`] = 0;
  studentProgress.value[`${qid}_Failed`] = true;
  localStorage.setItem('mds_student_progress', JSON.stringify(studentProgress.value));
  syncToSheets();
};

const projectUploadType = ref('link');
const projectLink = ref('');
const projectFile = ref(null);
const projectUploadStatus = ref('');
const projectUploadMessage = ref('');
const isUploading = ref(false);

const ideaObs = ref('');
const ideaSol = ref('');
const ideaUIFile = ref(null);
const ideaUploadStatus = ref('');
const ideaUploadMessage = ref('');
const isUploadingIdea = ref(false);
const handleProjectFileChange = (e) => {
  const file = e.target.files[0];
  if (file) {
    if (!file.name.endsWith('.aia')) {
      projectUploadMessage.value = 'Hanya menerima file berekstensi .aia';
      projectUploadStatus.value = 'error';
      e.target.value = null;
      projectFile.value = null;
      return;
    }
    projectFile.value = file;
    projectUploadStatus.value = '';
    projectUploadMessage.value = '';
  }
};

const submitProject = async () => {
  if (projectUploadType.value === 'link') {
    if (!projectLink.value.startsWith('https://gallery.appinventor.mit.edu/?galleryid')) {
      projectUploadStatus.value = 'error';
      projectUploadMessage.value = 'Link galeri tidak valid. Pastikan formatnya https://gallery.appinventor.mit.edu/?galleryid...';
      return;
    }
    isUploading.value = true;
    try {
      const fileCol = 'Project1_Code';
      saveProgress(fileCol, projectLink.value);
      projectUploadStatus.value = 'success';
      projectUploadMessage.value = 'Link project berhasil disimpan!';
      console.log(`[DEBUG] Link project berhasil diunggah dan disimpan ke kolom ${fileCol}. URL:`, projectLink.value);
    } catch (e) {
      projectUploadStatus.value = 'error';
      projectUploadMessage.value = 'Gagal menyimpan: ' + e.message;
    } finally {
      isUploading.value = false;
    }
  } else {
    if (!projectFile.value) {
      projectUploadStatus.value = 'error';
      projectUploadMessage.value = 'Silakan pilih file .aia terlebih dahulu';
      return;
    }
    isUploading.value = true;
    projectUploadStatus.value = '';
    projectUploadMessage.value = 'Sedang mengunggah file... mohon tunggu';
    
    const reader = new FileReader();
    reader.onload = async (e) => {
      const base64Data = e.target.result;
      const projName = 'mini project';
      const fileNameStr = `${studentData.value.name}_${studentData.value.school}_grupD_${projName}_${projectFile.value.name}`;
      const fileCol = 'Project1_Code';
      
      const payload = {
        Group: 'gms2d',
        Students_Email: studentData.value.email,
        Students_Name: studentData.value.name,
        Students_School: studentData.value.school,
        fileData: base64Data,
        fileName: fileNameStr,
        mimeType: 'application/octet-stream',
        fileColumn: fileCol
      };
      
      try {
        const response = await fetch(APP_SCRIPT_URL, {
          method: 'POST',
          body: JSON.stringify(payload),
          headers: { 'Content-Type': 'text/plain;charset=utf-8' }
        });
        const result = await response.json();
        if (result.success) {
          projectUploadStatus.value = 'success';
          projectUploadMessage.value = 'File project berhasil diunggah!';
          console.log(`[DEBUG] File project ${fileNameStr} berhasil diunggah dan disimpan ke kolom ${fileCol}. URL:`, result.fileUrl);
          saveProgress(fileCol, result.fileUrl || 'uploaded_aia'); 
        } else {
          throw new Error(result.message);
        }
      } catch (err) {
        projectUploadStatus.value = 'error';
        projectUploadMessage.value = 'Gagal mengunggah: ' + err.message;
      } finally {
        isUploading.value = false;
      }
    };
    reader.onerror = () => {
      projectUploadStatus.value = 'error';
      projectUploadMessage.value = 'Gagal membaca file';
      isUploading.value = false;
    };
    reader.readAsDataURL(projectFile.value);
  }
};

const handleIdeaUIFileChange = (e) => {
  const file = e.target.files[0];
  if (file) {
    if (!file.type.startsWith('image/')) {
      ideaUploadMessage.value = 'Hanya menerima file gambar (JPG/PNG)';
      ideaUploadStatus.value = 'error';
      e.target.value = null;
      ideaUIFile.value = null;
      return;
    }
    ideaUIFile.value = file;
    ideaUploadStatus.value = '';
    ideaUploadMessage.value = '';
  }
};

const submitIdea = async () => {
  if (!ideaObs.value.trim() || !ideaSol.value.trim()) {
    ideaUploadStatus.value = 'error';
    ideaUploadMessage.value = 'Pastikan kamu sudah mengisi Text Box 1 dan Text Box 2';
    return;
  }
  if (!ideaUIFile.value) {
    ideaUploadStatus.value = 'error';
    ideaUploadMessage.value = 'Silakan pilih gambar desain UI kamu (JPG/PNG)';
    return;
  }
  
  isUploadingIdea.value = true;
  ideaUploadStatus.value = '';
  ideaUploadMessage.value = 'Sedang mengirim idemu... mohon tunggu';
  
  // Save text inputs directly to sheets via syncToSheets implicitly inside saveProgress
  saveProgress('Idea_Obs', ideaObs.value);
  saveProgress('Idea_Sol', ideaSol.value);
  
  const reader = new FileReader();
  reader.onload = async (e) => {
    const base64Data = e.target.result;
    const projName = 'ide_aplikasi';
    const fileNameStr = `${studentData.value.name}_${studentData.value.school}_grupD_${projName}_${ideaUIFile.value.name}`;
    const fileCol = 'Idea_UI_Code';
    
    const payload = {
      Group: 'gms2d',
      Students_Email: studentData.value.email,
      Students_Name: studentData.value.name,
      Students_School: studentData.value.school,
      fileData: base64Data,
      fileName: fileNameStr,
      mimeType: ideaUIFile.value.type,
      fileColumn: fileCol
    };
    
    try {
      const response = await fetch(APP_SCRIPT_URL, {
        method: 'POST',
        body: JSON.stringify(payload),
        headers: { 'Content-Type': 'text/plain;charset=utf-8' }
      });
      const result = await response.json();
      if (result.success) {
        ideaUploadStatus.value = 'success';
        ideaUploadMessage.value = 'Ide aplikasi dan gambar desainmu berhasil dikirim! Keren 🚀';
        saveProgress(fileCol, result.fileUrl || 'uploaded_image'); 
      } else {
        throw new Error(result.message);
      }
    } catch (err) {
      ideaUploadStatus.value = 'error';
      ideaUploadMessage.value = 'Gagal mengirim: ' + err.message;
    } finally {
      isUploadingIdea.value = false;
    }
  };
  reader.onerror = () => {
    ideaUploadStatus.value = 'error';
    ideaUploadMessage.value = 'Gagal membaca file gambar';
    isUploadingIdea.value = false;
  };
  reader.readAsDataURL(ideaUIFile.value);
};


const syncToSheets = async () => {
  if (!isLoggedIn.value) return;
  const payload = {
    Students_Email: studentData.value.email,
    Students_Name: studentData.value.name,
    Students_School: studentData.value.school,
    Group: 'gms2d',
    ...studentProgress.value
  };
  try {
    await fetch(APP_SCRIPT_URL, {
      method: 'POST',
      body: JSON.stringify(payload),
      headers: { 'Content-Type': 'text/plain;charset=utf-8' } // text/plain untuk bypass CORS AppScript
    });
    console.log('[DEBUG] Progress berhasil dikirim (sync) ke Google Sheets:', payload);
  } catch(err) {
    console.error("Sync error", err);
  }
};

const handleLogin = async () => {
  if (!selectedSchool.value || !loginEmail.value.trim()) {
    loginErrorTitle.value = 'Lengkapi dulu ya';
    loginErrorMessage.value = 'Pilih sekolah, lalu masukkan email yang terdaftar di Akademia Ruangguru.';
    showLoginError.value = true;
    return;
  }
  
  isLoggingIn.value = true;
  showLoginError.value = false;
  loginEmailSuggestion.value = null;

  try {
    const nextAttempt = loginEmailAttempts.value + 1;
    const params = new URLSearchParams({
      action: 'login',
      school: selectedSchool.value,
      email: loginEmail.value,
      attempts: String(nextAttempt)
    });
    const res = await fetch(`${APP_SCRIPT_URL}?${params.toString()}`);
    const data = await res.json();
    if (data.success) {
      studentData.value = { name: data.name, school: data.school, email: data.email };
      isLoggedIn.value = true;
      loginEmailAttempts.value = 0;
      localStorage.setItem('mds_student_login', JSON.stringify(studentData.value));
    } else {
      loginEmailAttempts.value = nextAttempt;
      loginErrorTitle.value = data.needsRfo ? 'Perlu bantuan RFO' : 'Email belum cocok';
      loginErrorMessage.value = data.message || 'Email ini belum cocok dengan data Akademia Ruangguru untuk sekolah yang dipilih. Coba cek lagi penulisannya ya.';
      loginEmailSuggestion.value = data.suggestion || null;
      showLoginError.value = true;
    }
  } catch (err) {
    console.error("Login error", err);
    loginErrorTitle.value = 'Belum bisa masuk';
    loginErrorMessage.value = 'Koneksi ke data siswa belum berhasil. Coba lagi sebentar ya.';
    showLoginError.value = true;
  } finally {
    isLoggingIn.value = false;
  }
};

const fetchSchoolOptions = async (query = loginSchool.value) => {
  const requestId = ++schoolSearchRequestId;
  isSchoolLoading.value = true;
  try {
    const params = new URLSearchParams({ action: 'schools', query });
    const res = await fetch(`${APP_SCRIPT_URL}?${params.toString()}`);
    const data = await res.json();
    if (requestId === schoolSearchRequestId && data.success) schoolOptions.value = data.schools || [];
  } catch (err) {
    console.error("School search error", err);
  } finally {
    if (requestId === schoolSearchRequestId) isSchoolLoading.value = false;
  }
};

const fetchEmailHelpResults = async (query = emailHelpQuery.value) => {
  if (!selectedSchool.value || !query.trim()) {
    emailHelpResults.value = [];
    return;
  }
  isEmailHelpLoading.value = true;
  try {
    const params = new URLSearchParams({ action: 'students', school: selectedSchool.value, query });
    const res = await fetch(`${APP_SCRIPT_URL}?${params.toString()}`);
    const data = await res.json();
    if (data.success) emailHelpResults.value = data.students || [];
  } catch (err) {
    console.error("Email help search error", err);
  } finally {
    isEmailHelpLoading.value = false;
  }
};

const handleSchoolInput = () => {
  selectedSchool.value = '';
  loginEmail.value = '';
  emailHelpQuery.value = '';
  emailHelpResults.value = [];
  isSchoolDropdownOpen.value = true;
  loginEmailAttempts.value = 0;
  loginEmailSuggestion.value = null;
  showLoginError.value = false;
  if (schoolSearchTimer) clearTimeout(schoolSearchTimer);
  schoolSearchTimer = setTimeout(() => fetchSchoolOptions(), 250);
};

const handleEmailInput = () => {
  loginEmailSuggestion.value = null;
  showLoginError.value = false;
};

const handleEmailHelpInput = () => {
  fetchEmailHelpResults();
};

const openSchoolDropdown = () => {
  isSchoolDropdownOpen.value = true;
  fetchSchoolOptions('');
};

const closeSchoolDropdownSoon = () => {
  setTimeout(() => {
    isSchoolDropdownOpen.value = false;
  }, 120);
};

const selectSchool = (school) => {
  loginSchool.value = school;
  selectedSchool.value = school;
  loginEmail.value = '';
  emailHelpQuery.value = '';
  emailHelpResults.value = [];
  isSchoolDropdownOpen.value = false;
  loginEmailAttempts.value = 0;
  loginEmailSuggestion.value = null;
  showLoginError.value = false;
};

const toggleEmailHelp = () => {
  emailHelpOpen.value = !emailHelpOpen.value;
  if (!emailHelpOpen.value) return;
  emailHelpQuery.value = '';
  emailHelpResults.value = [];
};


onUnmounted(() => {
  window.removeEventListener('resize', updateWidth);
});

const handleLogout = () => {
  localStorage.removeItem('mds_student_login');
  isLoggedIn.value = false;
  loginSchool.value = '';
  loginEmail.value = '';
  selectedSchool.value = '';
  isSchoolDropdownOpen.value = false;
  loginEmailAttempts.value = 0;
  loginEmailSuggestion.value = null;
  emailHelpOpen.value = false;
  emailHelpQuery.value = '';
  emailHelpResults.value = [];
  studentData.value = { email: '', name: '', school: '' };
};


onMounted(() => {
  window.addEventListener('resize', updateWidth);

  const savedLogin = localStorage.getItem('mds_student_login');
  if (savedLogin) {
    studentData.value = JSON.parse(savedLogin);
    isLoggedIn.value = true;
  }
  const savedProgress = localStorage.getItem('mds_student_progress');
  if (savedProgress) {
    studentProgress.value = JSON.parse(savedProgress);
  }
});

const videoWatchedStatus = ref({
  1: false, 2: false, 3: false, 4: false, 5: false, 6: false, 7: false
});

const youtubeReady = ref(false);
const players = {};
const timeCheckers = {};


const introRefs = ref({});
const introPlayed = ref({ 1: true, 2: true, 3: true, 4: true, 5: true });
const introVideoSrc = import.meta.env.BASE_URL + 'intro.mp4';

const playerStates = ref({
  1: { isPlaying: false, currentTime: 0, duration: 0, isMuted: false, isReady: false, isError: false, hasStarted: false, isBuffering: false },
  2: { isPlaying: false, currentTime: 0, duration: 0, isMuted: false, isReady: false, isError: false, hasStarted: false, isBuffering: false },
  3: { isPlaying: false, currentTime: 0, duration: 0, isMuted: false, isReady: false, isError: false, hasStarted: false, isBuffering: false },
  4: { isPlaying: false, currentTime: 0, duration: 0, isMuted: false, isReady: false, isError: false, hasStarted: false, isBuffering: false },
  5: { isPlaying: false, currentTime: 0, duration: 0, isMuted: false, isReady: false, isError: false, hasStarted: false, isBuffering: false },
  6: { isPlaying: false, currentTime: 0, duration: 0, isMuted: false, isReady: false, isError: false, hasStarted: false, isBuffering: false },
  7: { isPlaying: false, currentTime: 0, duration: 0, isMuted: false, isReady: false, isError: false, hasStarted: false, isBuffering: false },
});

const isFullscreen = ref(false);
const videoContainers = ref({});

// Quiz Overlay States
const quizState = ref({
  isOpen: false,
  shuffledQuestions: [],
  currentQuestionIdx: 0,
  resumeVideoAfterQuiz: false,
  resumeVideoTime: null,
  quizFeedback: '',
  quizFeedbackType: '',
  isNextBtnVisible: false,
  nextBtnText: 'Soal berikutnya →',
  activeQuizConfig: null,
  activeQuizStep: null,
  replayingQuizVideo: false,
  replayCheckpointArmed: false,
  choicesDisabled: false,
  selectedChoice: null,
  shownQuizzes: {}
});

const quizReturn = ref({
  isVisible: false
});

const showCompletionToast = ref(false);
const failedAttempts = ref({});

// Time formatting helper
const formatVideoTime = (value) => {
  const totalSeconds = Number.isFinite(value) ? Math.max(0, Math.floor(value)) : 0;
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = String(totalSeconds % 60).padStart(2, "0");
  return minutes + ":" + seconds;
};

const getBookmarks = (stepId) => {
  return courseData[stepId]?.bookmarks || [];
};

const getVideoStartBoundary = (stepId) => {
  return courseData[stepId]?.startSeconds || 0;
};

const getVideoEndBoundary = (stepId) => {
  const rawDuration = playerStates.value[stepId]?.rawDuration || 0;
  return courseData[stepId]?.endSeconds || rawDuration;
};

// Seek boundary enforcement
const enforceVideoStartBoundary = (stepId) => {
  const player = players[stepId];
  if (!player || typeof player.getCurrentTime !== "function" || typeof player.seekTo !== "function") return;
  const startBoundary = getVideoStartBoundary(stepId);
  const endBoundary = courseData[stepId]?.endSeconds || 0; // Only enforce if endSeconds explicitly provided
  const currentTime = player.getCurrentTime();

  if (startBoundary > 0 && currentTime < startBoundary - 0.5) {
    player.seekTo(startBoundary, true);
  } else if (endBoundary > 0 && currentTime >= endBoundary) {
    player.pauseVideo();
    
    // Set video as watched since it hit the artificial end boundary
    if (!videoWatchedStatus.value[stepId]) {
      videoWatchedStatus.value[stepId] = true;
      console.log(`[DEBUG] Video ${stepId} reached endBoundary (${endBoundary}s). Marked as watched.`);
      checkVideoQuizzes(stepId);
    }
    
    // Keep it at endBoundary
    if (currentTime > endBoundary + 0.5) {
      player.seekTo(endBoundary, true);
    }
  }

  // Skip logic: if the user rewinds into a segment that was skipped by a quiz, push them out
  const stepConfig = courseData[stepId];
  if (stepConfig && stepConfig.quizzes) {
    for (const quiz of stepConfig.quizzes) {
      if (quiz.skipTo && currentTime >= quiz.time + 0.5 && currentTime < quiz.skipTo - 0.5) {
        player.seekTo(quiz.skipTo, true);
        break; // Only seek once per cycle
      }
    }
  }
};

const restartVideoFromBoundary = (stepId, shouldPlay = true) => {
  const player = players[stepId];
  if (!player || typeof player.seekTo !== "function") return;

  const startBoundary = getVideoStartBoundary(stepId);
  player.seekTo(startBoundary, true);
  playerStates.value[stepId].currentTime = startBoundary;
  playerStates.value[stepId].progress = getSeekValue(stepId);

  if (shouldPlay && typeof player.playVideo === "function") {
    player.playVideo();
  }
};

const updateVideoControls = (stepId) => {
  enforceVideoStartBoundary(stepId);
  const player = players[stepId];
  if (!player || typeof player.getCurrentTime !== "function") return;

  const rawDuration = player.getDuration() || 0;
  playerStates.value[stepId].rawDuration = rawDuration;

  const startBoundary = getVideoStartBoundary(stepId);
  const endBoundary = getVideoEndBoundary(stepId) || rawDuration;

  const currentTime = player.getCurrentTime() || 0;
  
  const effectiveDuration = Math.max(0, endBoundary - startBoundary);
  const effectiveCurrentTime = Math.max(0, Math.min(currentTime, endBoundary) - startBoundary);

  playerStates.value[stepId].duration = effectiveDuration;
  playerStates.value[stepId].currentTime = effectiveCurrentTime;
  playerStates.value[stepId].progress = getSeekValue(stepId);
  playerStates.value[stepId].durationFormatted = formatVideoTime(effectiveDuration);
  playerStates.value[stepId].currentTimeFormatted = formatVideoTime(effectiveCurrentTime);
  
  const percentage = effectiveDuration > 0 ? (effectiveCurrentTime / effectiveDuration) : 0;
  const hasQuiz = courseData[stepId]?.quizzes?.length > 0;
  const requiredPercentage = hasQuiz ? 0.90 : 0.95;

  if (percentage >= requiredPercentage && !videoWatchedStatus.value[stepId]) {
    videoWatchedStatus.value[stepId] = true;
    console.log(`[DEBUG] Video ${stepId} reached required watch percentage (${requiredPercentage * 100}%). Marked as watched.`);
  }

  const now = Date.now();
  if (!window._lastDebugLogTime) window._lastDebugLogTime = {};
  if (now - (window._lastDebugLogTime[stepId] || 0) > 2000) {
    const quizProgress = getStepQuizProgress(stepId);
    console.log(`[DEBUG] Step ${stepId} | Video Watched: ${!!videoWatchedStatus.value[stepId]} | Quizzes: ${quizProgress.recordedCompletedCount}/${quizProgress.total}`);
    window._lastDebugLogTime[stepId] = now;
  }
};

const getSeekMin = (stepId) => {
  const duration = playerStates.value[stepId].duration || 0;
  const startBoundary = getVideoStartBoundary(stepId);
  return duration && startBoundary ? (startBoundary / duration * 100) : 0;
};

const getSeekValue = (stepId) => {
  const duration = playerStates.value[stepId].duration || 0;
  const currentTime = playerStates.value[stepId].currentTime || 0;
  return duration ? (currentTime / duration * 100) : 0;
};

// Video actions
const playIntroThenVideo = async (stepId) => {
  const introEl = introRefs.value[stepId];
  if (introEl && !introPlayed.value[stepId]) {
    playerStates.value[stepId].introPlaying = true;
    playerStates.value[stepId].hasStarted = true;
    await nextTick();
    introEl.currentTime = 0;
    introEl.play().catch(e => {
      console.error("Intro video play error:", e);
      onIntroEnded(stepId);
    });
  } else {
    console.warn("No introEl or already played for step", stepId);
    onIntroEnded(stepId);
  }
};

const onIntroEnded = (stepId) => {
  playerStates.value[stepId].introPlaying = false;
  introPlayed.value[stepId] = true;
  
  const player = players[stepId];
  if (!player || typeof player.getPlayerState !== "function") {
    initializeYouTubePlayer(stepId);
    setTimeout(() => {
      if (players[stepId] && typeof players[stepId].playVideo === 'function') {
         players[stepId].playVideo();
      }
    }, 500);
  } else {
    player.playVideo();
  }
};

const playVideo = (stepId) => {
  if (!introPlayed.value[stepId]) {
    playIntroThenVideo(stepId);
    return;
  }
  playerStates.value[stepId].hasStarted = true;
  const player = players[stepId];
  if (!player || typeof player.getPlayerState !== "function") {
    initializeYouTubePlayer(stepId);
    // YouTube player onReady will not autoplay unless we tell it to,
    // but the player itself is now visible so the user can click it or we can play it if ready.
    setTimeout(() => {
      if (players[stepId] && typeof players[stepId].playVideo === 'function') {
         players[stepId].playVideo();
      }
    }, 500);
    return;
  }
  player.playVideo();
};
const togglePlay = (stepId) => {
  if (!introPlayed.value[stepId]) {
    playIntroThenVideo(stepId);
    return;
  }
  const player = players[stepId];
  if (!player || typeof player.getPlayerState !== "function") {
    initializeYouTubePlayer(stepId);
    return;
  }
  if (playerStates.value[stepId].isPlaying) {
    player.pauseVideo();
  } else {
    player.playVideo();
  }
};

const toggleMute = (stepId) => {
  const player = players[stepId];
  if (!player || typeof player.isMuted !== "function") return;
  if (player.isMuted()) {
    player.unMute();
    playerStates.value[stepId].isMuted = false;
  } else {
    player.mute();
    playerStates.value[stepId].isMuted = true;
  }
};

const onSeekInput = (stepId, event) => {
  const player = players[stepId];
  if (!player || typeof player.seekTo !== "function") return;
  const duration = playerStates.value[stepId].duration || 0;
  const startBoundary = getVideoStartBoundary(stepId);
  const offsetTime = (duration * Number(event.target.value)) / 100;
  player.seekTo(startBoundary + offsetTime, true);
};

const toggleFullscreen = (stepId) => {
  const el = document.querySelector(`.video-frame[data-video-step="${stepId}"]`);
  if (!el) return;
  if (document.fullscreenElement) {
    document.exitFullscreen();
  } else {
    el.requestFullscreen();
  }
};

const seekToBookmark = (stepId, time) => {
  const player = players[stepId];
  if (player && typeof player.seekTo === "function") {
    player.seekTo(time, true);
    if (typeof player.playVideo === "function") player.playVideo();
    
    const container = videoContainers.value[stepId];
    if (container) {
      container.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  }
};

// YouTube player setup
const initializeYouTubePlayer = (stepId) => {
  const normalizedStepId = String(stepId);
  if (!youtubeReady.value || players[normalizedStepId] || !courseData[normalizedStepId]) return;

  const playerId = "youtube-player-" + normalizedStepId;
  const domEl = document.getElementById(playerId);
  if (!domEl) return;

  playerStates.value[normalizedStepId].isError = false;

  players[normalizedStepId] = new window.YT.Player(playerId, {
    videoId: courseData[normalizedStepId].videoId,
    playerVars: {
      playsinline: 1,
      rel: 0,
      controls: 0,
      vq: 'hd1080',
      disablekb: 1,
      fs: 0,
      iv_load_policy: 3,
      start: courseData[normalizedStepId].startSeconds || 0,
      origin: window.location.origin
    },
    events: {
      onReady: (event) => {
        const iframe = event.target.getIframe();
        iframe.removeAttribute("allowfullscreen");
        iframe.setAttribute("tabindex", "-1");
        iframe.setAttribute("aria-hidden", "true");
        
        playerStates.value[normalizedStepId].isReady = true;
        playerStates.value[normalizedStepId].duration = event.target.getDuration() || 0;
        
        enforceVideoStartBoundary(normalizedStepId);
        updateVideoControls(normalizedStepId);
      },
      onError: () => {
        playerStates.value[normalizedStepId].isError = true;
      },
      onStateChange: (event) => handlePlayerStateChange(normalizedStepId, event)
    }
  });
};

const handlePlayerStateChange = (stepId, event) => {
  const isPlaying = event.data === window.YT.PlayerState.PLAYING;
  const isBuffering = event.data === window.YT.PlayerState.BUFFERING;
  playerStates.value[stepId].isBuffering = isBuffering;
  playerStates.value[stepId].isPlaying = isPlaying;

  if (isPlaying) {
    playerStates.value[stepId].hasStarted = true;
    enforceVideoStartBoundary(stepId);
  }

  if (event.data === window.YT.PlayerState.ENDED) {
    videoWatchedStatus.value[stepId] = true;
    checkVideoQuizzes(stepId);
    
    restartVideoFromBoundary(stepId, false);
    
    introPlayed.value[stepId] = false;
    playerStates.value[stepId].hasStarted = false;
    playerStates.value[stepId].isPlaying = false;
    
    return;
  }

  updateVideoControls(stepId);

  window.clearInterval(timeCheckers[stepId]);
  if (isPlaying) {
    timeCheckers[stepId] = window.setInterval(() => {
      updateVideoControls(stepId);
      checkVideoQuizzes(stepId);
    }, 300);
  }
};

const checkVideoQuizzes = (stepId) => {
  const player = players[stepId];
  if (!player || typeof player.getCurrentTime !== 'function') return;

  const currentTime = player.getCurrentTime();
  const stepConfig = courseData[stepId];
  if (!stepConfig || !stepConfig.quizzes) return;

  for (let idx = 0; idx < stepConfig.quizzes.length; idx++) {
    const quiz = stepConfig.quizzes[idx];
    const quizKey = `${stepId}_${idx}`;
    if (quizState.value.replayingQuizVideo && quiz === quizState.value.activeQuizConfig) {
      if (currentTime < quiz.time - 0.5) {
        quizState.value.replayCheckpointArmed = true;
      }
      if (!quizState.value.replayCheckpointArmed) continue;
    }

    if (!quizState.value.shownQuizzes[quizKey] && currentTime >= quiz.time) {
      quizState.value.shownQuizzes[quizKey] = true;
      player.pauseVideo();
      window.clearInterval(timeCheckers[stepId]);

      const shouldResume = quiz.resume !== undefined ? quiz.resume : true;
      openQuiz(quiz.questions, shouldResume, quiz.resumeTime, quiz, stepId);
      return true;
    }
  }

  return false;
};

// Quiz Functions
const shuffle = (items) => {
  const result = [...items];
  for (let i = result.length - 1; i > 0; i--) {
    const randomIndex = Math.floor(Math.random() * (i + 1));
    [result[i], result[randomIndex]] = [result[randomIndex], result[i]];
  }
  return result;
};

const openQuiz = (questionsArray, shouldResume = false, seekTime = null, quizConfig = null, stepId = currentStep.value) => {
  console.log(`[DEBUG] Pop-up kuis muncul. Mode Resume: ${shouldResume}, Step: ${stepId}`);
  try {
    if (document.fullscreenElement) {
      const exitPromise = document.exitFullscreen();
      if (exitPromise !== undefined) exitPromise.catch(e => console.log(e));
    } else if (document.webkitFullscreenElement && document.webkitExitFullscreen) {
      document.webkitExitFullscreen();
    }
  } catch (err) {
    console.log('Exit fullscreen error:', err);
  }

  if (quizConfig) {
    quizState.value.activeQuizConfig = quizConfig;
    quizState.value.activeQuizStep = Number(stepId);
  } else {
    quizState.value.activeQuizConfig = null;
    quizState.value.activeQuizStep = null;
  }

  quizState.value.replayingQuizVideo = false;
  quizState.value.replayCheckpointArmed = false;
  quizReturn.value.isVisible = false;

  quizState.value.resumeVideoAfterQuiz = shouldResume;
  quizState.value.resumeVideoTime = seekTime;

  quizState.value.shuffledQuestions = shuffle([...questionsArray]);
  quizState.value.currentQuestionIdx = 0;
  quizState.value.isOpen = true;
  sheet.sequence.play({ direction: 'normal', range: [0, 0.4] });
  quizState.value.choicesDisabled = false;
  quizState.value.selectedChoice = null;
  quizState.value.quizFeedback = '';
  quizState.value.quizFeedbackType = '';
  quizState.value.isNextBtnVisible = false;
  quizState.value.nextBtnText = 'Soal berikutnya →';

  nextTick(() => {
    renderQuestion();
  });
};

const closeQuiz = (resumeVideo = false, seekTime = null) => {
  sheet.sequence.play({ direction: 'reverse', range: [0, 0.4] }).then(() => {
    quizState.value.isOpen = false;
  });
  if (resumeVideo && players[currentStep.value]) {
    const player = players[currentStep.value];
    if (seekTime !== null && typeof player.seekTo === "function") {
      player.seekTo(seekTime, true);
    }
    if (typeof player.playVideo === "function") {
      player.playVideo();
    }
  }
};

const currentQuestion = computed(() => {
  const questions = quizState.value.shuffledQuestions;
  const idx = quizState.value.currentQuestionIdx;
  if (questions && questions.length > 0 && idx < questions.length) {
    return questions[idx];
  }
  return null;
});

const getQuestionChoices = (question) => {
  if (!question) return [];
  const opts = question.choices || question.options;
  if (Array.isArray(opts) && opts.length > 0) return opts;
  if (typeof question.answer === "boolean") return ["True", "False"];
  return [];
};

const isQuizFinished = computed(() => {
  return quizState.value.shuffledQuestions.length > 0 && 
         quizState.value.currentQuestionIdx >= quizState.value.shuffledQuestions.length;
});

const attachCustomHtmlListeners = () => {
  setTimeout(() => { // ensure DOM is fully updated
    document.querySelectorAll('.answer-opt-btn').forEach(btn => {
      btn.onclick = function() {
        this.innerHTML = "Memeriksa...";
        const isCorrect = this.getAttribute('data-correct') === 'true';
        const expl = this.getAttribute('data-explanation');
        if (window.checkGuess) window.checkGuess(this, isCorrect, expl);
      };
    });

    const wrapHandler = (btnId, handlerFn) => {
      const btn = document.getElementById(btnId);
      if (btn) {
        btn.onclick = function() {
          const originalText = this.innerHTML;
          this.innerHTML = "Memeriksa...";
          handlerFn(this);
          // Restore text after 1 second if still enabled
          setTimeout(() => { if (!this.disabled) this.innerHTML = originalText; }, 1000);
        };
      }
    };

    wrapHandler('mb1-check-btn', (btn) => {
      const kw = document.getElementById('mb1-kw');
      const cond = document.getElementById('mb1-cond');
      if (window.checkMB1QGuess) window.checkMB1QGuess(kw ? kw.value : '', cond ? cond.value : '', btn, 'Syarat yang benar adalah elif dan age < 18.');
    });
    wrapHandler('mb2-check-btn', (btn) => {
      const v1 = document.getElementById('mb2-val1');
      const v2 = document.getElementById('mb2-val2');
      if (window.checkMB2QGuess) window.checkMB2QGuess(v1 ? v1.value : '', v2 ? v2.value : '', btn, 'Kondisi yang lebih ketat harus ditaruh di atas!');
    });
    wrapHandler('paren-check-btn', (btn) => {
      const input = document.getElementById('paren-input');
      if (window.checkParenGuess) window.checkParenGuess(input ? input.value : '', btn, 'Kita harus mengevaluasi or di dalam kurung terlebih dahulu.');
    });
    wrapHandler('and-check-btn', (btn) => {
      const input = document.getElementById('and-input');
      if (window.checkAndGuess) window.checkAndGuess(input ? input.value : '', btn, 'Kedua syarat harus terpenuhi untuk mendapatkan beasiswa.');
    });
    wrapHandler('or-check-btn', (btn) => {
      const input = document.getElementById('or-input');
      if (window.checkOrGuess) window.checkOrGuess(input ? input.value : '', btn, 'Salah satu syarat harus terpenuhi.');
    });
    wrapHandler('logical-check-btn', (btn) => {
      const input = document.getElementById('logical-input');
      if (window.checkNestedToLogicalGuess) window.checkNestedToLogicalGuess(input ? input.value : '', btn, 'Dengan operator and kita bisa menggabungkan dua if bersarang.');
    });
    wrapHandler('needs-check-btn', (btn) => {
      if (window.checkNeedsWantsGuess) window.checkNeedsWantsGuess('needs-input', btn);
    });
    wrapHandler('wants-check-btn', (btn) => {
      if (window.checkNeedsWantsGuess) window.checkNeedsWantsGuess('wants-input', btn);
    });
    wrapHandler('ide6-run-btn', (btn) => {
      if (window.runPyodideCode) window.runPyodideCode('python-ide-6', 'ide-output-6');
    });
    wrapHandler('ide6-submit-btn', (btn) => {
      if (window.checkIde6Guess) window.checkIde6Guess(btn);
    });
  }, 100);
};

const renderQuestion = () => {
  if (currentQuestion.value && !currentQuestion.value.html) {
    nextTick(() => {
      const trueBtn = document.querySelector('.choice-btn.true-btn');
      if (trueBtn) trueBtn.focus();
    });
  } else if (currentQuestion.value && currentQuestion.value.html) {
    nextTick(() => {
      attachCustomHtmlListeners();
    });
  }
};

const revealQuizNext = (label = "Soal berikutnya →") => {
  quizState.value.nextBtnText = label;
  quizState.value.isNextBtnVisible = true;
  
  nextTick(() => {
    const nextBtn = document.querySelector('.quiz-next-btn');
    if (nextBtn) {
      nextBtn.scrollIntoView({ behavior: "smooth", block: "nearest" });
      nextBtn.focus({ preventScroll: true });
    }
  });
};

const registerFailedInputAttempt = (btn, feedbackEl) => {
  const key = btn.id || btn.className || 'default-btn';
  const attempts = (failedAttempts.value[key] || 0) + 1;
  failedAttempts.value[key] = attempts;
  quizState.value.isNextBtnVisible = false;

  const attemptStatus = document.createElement("div");
  attemptStatus.className = "attempt-status";

  attemptStatus.classList.add("limit-reached");
  if (currentQuestion.value?.qid) {
    markQuestionFailed(currentQuestion.value?.qid);
  }
  attemptStatus.innerHTML = "Jawabanmu belum tepat. Coba cek lagi perlahan dan perhatikan petunjuk dari video.";
  revealQuizNext("Lanjut →");
  btn.disabled = true;
  btn.style.opacity = "0.55";

  feedbackEl.appendChild(attemptStatus);
};

const handleStandardAnswer = (answer) => {
  const item = currentQuestion.value;
  if (!item) return;
  if (quizState.value.choicesDisabled) return;

  const expectedAnswer = item.answer ?? item.correct;
  const normalizedAnswer = typeof answer === "string" ? answer.trim().toLowerCase() : answer;
  const normalizedExpected = typeof expectedAnswer === "string" ? expectedAnswer.trim().toLowerCase() : expectedAnswer;
  const isCorrect = normalizedAnswer === normalizedExpected;
  const attKey = item.qid ? `${item.qid}_Att` : null;
  const attempts = item.qid
    ? (studentProgress.value[attKey] || 0) + 1
    : (failedAttempts.value[item.question] || 0) + 1;
  
  quizState.value.selectedChoice = answer;
  if (item.qid) {
    studentProgress.value[attKey] = attempts;
    localStorage.setItem('mds_student_progress', JSON.stringify(studentProgress.value));
    syncToSheets();
  } else {
    failedAttempts.value[item.question] = attempts;
  }

  if (isCorrect) {
    quizState.value.choicesDisabled = true;
    quizState.value.quizFeedbackType = 'correct';
    quizState.value.quizFeedback = "Tepat. " + (item.explanation || "");
    if (item.qid) {
      saveProgress(`${item.qid}_Ans`, String(answer));
    }
    revealQuizNext();
  } else {
    quizState.value.quizFeedbackType = 'wrong';
    quizState.value.choicesDisabled = true;
    if (item.qid) {
      markQuestionFailed(item.qid);
    }
    quizState.value.quizFeedback = `Belum tepat. ${(item.explanation || "")}`;
    revealQuizNext("Lanjut →");
  }
};

const goToNextQuestion = () => {
  if (quizState.value.currentQuestionIdx + 1 >= quizState.value.shuffledQuestions.length) {
    closeQuiz(quizState.value.resumeVideoAfterQuiz, quizState.value.resumeVideoTime);
    return;
  }
  quizState.value.currentQuestionIdx += 1;
  quizState.value.choicesDisabled = false;
  quizState.value.selectedChoice = null;
  quizState.value.quizFeedback = '';
  quizState.value.quizFeedbackType = '';
  quizState.value.isNextBtnVisible = false;
  
  nextTick(() => {
    renderQuestion();
  });
};

const replayActiveQuizVideo = () => {
  if (!quizState.value.activeQuizConfig || quizState.value.activeQuizStep === null) return;

  const player = players[quizState.value.activeQuizStep];
  if (!player || typeof player.seekTo !== "function") return;

  const replayStart = Math.max(0, quizState.value.activeQuizConfig.time - 30);
  if (currentStep.value !== quizState.value.activeQuizStep) {
    currentStep.value = quizState.value.activeQuizStep;
  }

  quizState.value.activeQuizConfig.shown = false;
  quizState.value.replayingQuizVideo = true;
  quizState.value.replayCheckpointArmed = false;
  
  closeQuiz(false);
  quizReturn.value.isVisible = true;

  nextTick(() => {
    player.seekTo(replayStart, true);
    if (typeof player.playVideo === "function") {
      player.playVideo();
    }
    setTimeout(() => {
      if (!quizState.value.replayingQuizVideo || typeof player.getCurrentTime !== "function") return;
      if (Math.abs(player.getCurrentTime() - replayStart) > 2) {
        player.seekTo(replayStart, true);
      }
    }, 300);
  });
};

const returnToActiveQuiz = () => {
  if (!quizState.value.activeQuizConfig || quizState.value.activeQuizStep === null) return;

  const player = players[quizState.value.activeQuizStep];
  if (player && typeof player.pauseVideo === "function") {
    player.pauseVideo();
  }
  quizState.value.activeQuizConfig.shown = true;
  openQuiz(
    quizState.value.activeQuizConfig.questions,
    quizState.value.activeQuizConfig.resume !== undefined ? quizState.value.activeQuizConfig.resume : true,
    quizState.value.activeQuizConfig.resumeTime,
    quizState.value.activeQuizConfig,
    quizState.value.activeQuizStep
  );
};

// Pyodide Integration
const pyodideBaseUrl = "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/";
let pyodideReadyPromise = null;

function ensurePyodideScript() {
  if (typeof window.loadPyodide === "function") return Promise.resolve();

  return new Promise((resolve, reject) => {
    const existingScript = document.querySelector('script[data-pyodide-loader]');
    if (existingScript) {
      existingScript.addEventListener("load", resolve, { once: true });
      existingScript.addEventListener("error", reject, { once: true });
      return;
    }

    const script = document.createElement("script");
    script.src = pyodideBaseUrl + "pyodide.js";
    script.dataset.pyodideLoader = "true";
    script.addEventListener("load", resolve, { once: true });
    script.addEventListener("error", () => reject(new Error("Pyodide gagal dimuat.")), { once: true });
    document.head.appendChild(script);
  });
}

function initPyodide() {
  if (!pyodideReadyPromise) {
    pyodideReadyPromise = ensurePyodideScript()
      .then(() => window.loadPyodide({ indexURL: pyodideBaseUrl }));
  }
  return pyodideReadyPromise;
}

const runPyodideCode = async (inputId, outputId) => {
  const codeEl = document.getElementById(inputId);
  const outputEl = document.getElementById(outputId);
  if (!codeEl || !outputEl) return;
  outputEl.innerHTML = "Menjalankan...";
  outputEl.style.color = "white";

  try {
    let pyodide = await initPyodide();
    pyodide.setStdout({ batched: (msg) => {
      if (outputEl.innerHTML === "Menjalankan...") outputEl.innerHTML = "";
      outputEl.innerHTML += msg + "\n";
    }});
    
    await pyodide.runPythonAsync(codeEl.value);
    if (outputEl.innerHTML === "Menjalankan...") {
      outputEl.innerHTML = "Program selesai tanpa output teks.";
    }
  } catch (err) {
    outputEl.innerHTML = err;
    outputEl.style.color = "#FF4444";
  }
};

const exposeGlobalMethods = () => {
  const trackAttempt = (qid, answerStr, isCorrect) => {
    if(!qid) return;
    const attKey = qid + "_Att";
    const ansKey = qid + "_Ans";
    let att = (studentProgress.value[attKey] || 0) + 1;
    studentProgress.value[attKey] = att;
    
    // Mapping spesifik Video 6
    let finalAnsKey = ansKey;
    if (qid === 'V6_Q1') finalAnsKey = 'V6_Needs_Ans';
    if (qid === 'V6_Q2') finalAnsKey = 'V6_Wants_Ans';
    if (qid === 'V6_Q3') { finalAnsKey = 'V6_IDE_Code'; studentProgress.value['V6_IDE_Att'] = att; }
    
    if (isCorrect) {
      studentProgress.value[finalAnsKey] = answerStr;
    } else if (att >= 3) {
      studentProgress.value[finalAnsKey] = '0';
      studentProgress.value[`${qid}_Score`] = 0;
      studentProgress.value[`${qid}_Failed`] = true;
    }
    saveProgress(attKey, att); 
  };

  window.checkGuess = function(btn, isCorrect, explanation) {
    const qid = currentQuestion.value?.qid;
    trackAttempt(qid, btn.innerText, isCorrect);
    
    const container = btn.parentElement;
    const feedback = container.nextElementSibling;
    const buttons = container.querySelectorAll('button');
    buttons.forEach(b => {
      b.disabled = true;
      b.style.opacity = '0.5';
    });
    btn.style.opacity = '1';
    
    feedback.style.display = 'block';
    // NEW: Auto-scroll on mobile
    setTimeout(() => {
      if (window.innerWidth <= 650) {
        feedback.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }, 100);
    if (isCorrect) {
      feedback.innerHTML = `✅ <strong>TEPAT SEKALI!</strong><br>${explanation}`;
      feedback.style.backgroundColor = "#27c881";
      feedback.style.color = "var(--black)";
      revealQuizNext();
    } else {
      feedback.innerHTML = `❌ <strong>SALAH!</strong><br>${explanation}`;
      feedback.style.backgroundColor = "#ff5c8a";
      feedback.style.color = "white";
      const attempts = qid ? studentProgress.value[`${qid}_Att`] || 1 : 1;
      if (attempts >= 3) {
        markQuestionFailed(qid);
        feedback.innerHTML += `<br><strong>Sudah 3 kali mencoba.</strong> Kamu boleh lanjut dulu. Perhatikan lagi videonya sebelum masuk ke bagian berikutnya, ya.`;
        revealQuizNext("Lanjut →");
      } else {
        buttons.forEach(b => {
          b.disabled = false;
          b.style.opacity = '1';
        });
      }
    }
  };

  window.checkPasswordGuess = function(btn) {
    const qid = currentQuestion.value?.qid;
    const input = document.getElementById('pass-input');
    const val = input ? input.value : '';
    
    const container = btn.parentElement;
    const feedback = container.nextElementSibling;
    
    const hasNum = /\d/.test(val);
    const hasSym = /[^a-zA-Z0-9]/.test(val);
    const hasUpper = /[A-Z]/.test(val);
    const hasLower = /[a-z]/.test(val);
    
    feedback.style.display = 'block';
    // Auto-scroll on mobile
    setTimeout(() => {
      if (window.innerWidth <= 650) {
        feedback.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }, 100);

    if (val.length < 8) {
      feedback.innerHTML = `❌ <strong>Terlalu pendek!</strong><br>Password harus minimal 8 karakter.`;
      feedback.style.backgroundColor = "#ff5c8a";
      feedback.style.color = "white";
      registerFailedInputAttempt(btn, feedback);
      return;
    }
    if (!hasNum || !hasSym || !hasUpper || !hasLower) {
      feedback.innerHTML = `❌ <strong>Password belum kuat!</strong><br>Pastikan ada kombinasi huruf besar, huruf kecil, angka, dan simbol khusus (seperti !, @, #).`;
      feedback.style.backgroundColor = "#ff5c8a";
      feedback.style.color = "white";
      registerFailedInputAttempt(btn, feedback);
      return;
    }
    
    // Correct
    feedback.innerHTML = `✅ <strong>Password Kuat!</strong><br>Bagus sekali, kamu sudah mengerti cara membuat password yang tangguh!`;
    feedback.style.backgroundColor = "#27c881";
    feedback.style.color = "var(--black)";
    
    btn.disabled = true;
    btn.style.opacity = '0.5';
    if (input) input.disabled = true;
    
    // Track attempt and answer
    if (qid) {
      studentProgress.value[`${qid}_Ans`] = "completed";
      saveProgress(`${qid}_Ans`, "completed");
      saveProgress(`${qid}_Att`, 1);
    }
    revealQuizNext("Lanjut →");
  };

  window.checkMB1QGuess = function(kwVal, condVal, btn, explanation) {
    const qid = currentQuestion.value?.qid;
    let kw = kwVal.replace(/\s+/g, '').toLowerCase();
    let cond = condVal.replace(/\s+/g, '').toLowerCase();
    const isCorrect = (kw === 'elif' && (cond === 'age<18' || cond === 'age<=17'));
    trackAttempt(qid, `${kwVal} ${condVal}`, isCorrect);

    const container = btn.parentElement;
    const feedback = container.nextElementSibling;
    const isCorrectCondition = isCorrect;
    feedback.style.display = 'block';
    // NEW: Auto-scroll on mobile
    setTimeout(() => {
      if (window.innerWidth <= 650) {
        feedback.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }, 100);
    if (isCorrectCondition) {
      feedback.innerHTML = `✅ <strong>TEPAT SEKALI!</strong><br>${explanation}`;
      feedback.style.backgroundColor = "#27c881";
      feedback.style.color = "var(--black)";
      btn.disabled = true;
      btn.style.opacity = '0.5';
      const kwInput = document.getElementById('mb1-kw');
      const condInput = document.getElementById('mb1-cond');
      if (kwInput) kwInput.disabled = true;
      if (condInput) condInput.disabled = true;
      revealQuizNext();
    } else {
      feedback.innerHTML = `❌ <strong>KODE BELUM TEPAT!</strong><br>Coba lagi! Kata kunci percabangan yang dipakai adalah <code>elif</code> dan kondisinya mengecek apakah usia di bawah 18 tahun (<code>age &lt; 18</code>).`;
      feedback.style.backgroundColor = "#ff5c8a";
      feedback.style.color = "white";
      registerFailedInputAttempt(btn, feedback);
    }
  };

  window.checkMB2QGuess = function(val1, val2, btn, explanation) {
    const qid = currentQuestion.value?.qid;
    let v1 = val1.replace(/\s+/g, '');
    let v2 = val2.replace(/\s+/g, '');
    const isCorrect = (v1 === '90' && v2 === '80');
    trackAttempt(qid, `${val1} ${val2}`, isCorrect);

    const container = btn.parentElement;
    const feedback = container.nextElementSibling;
    feedback.style.display = 'block';
    // NEW: Auto-scroll on mobile
    setTimeout(() => {
      if (window.innerWidth <= 650) {
        feedback.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }, 100);
    if (isCorrect) {
      feedback.innerHTML = `✅ <strong>TEPAT SEKALI!</strong><br>${explanation}`;
      feedback.style.backgroundColor = "#27c881";
      feedback.style.color = "var(--black)";
      btn.disabled = true;
      btn.style.opacity = '0.5';
      const val1Input = document.getElementById('mb2-val1');
      const val2Input = document.getElementById('mb2-val2');
      if (val1Input) val1Input.disabled = true;
      if (val2Input) val2Input.disabled = true;
      revealQuizNext();
    } else {
      feedback.innerHTML = `❌ <strong>URUTAN MASIH SALAH!</strong><br>Ingat, kondisi paling ketat/sulit (nilai &gt;= 90 untuk A) harus dicek paling atas!`;
      feedback.style.backgroundColor = "#ff5c8a";
      feedback.style.color = "white";
      registerFailedInputAttempt(btn, feedback);
    }
  };

  window.checkParenGuess = function(userVal, btn, explanation) {
    const qid = currentQuestion.value?.qid;
    let normalizedUser = userVal.replace(/\s+/g, '').toLowerCase();
    const isCorrect = (normalizedUser === 'password_okand(is_adminoris_premium)' || normalizedUser === '(is_adminoris_premium)andpassword_ok' || normalizedUser === 'password_ok==trueand(is_admin==trueoris_premium==true)');
    trackAttempt(qid, userVal, isCorrect);

    const container = btn.parentElement;
    const feedback = container.nextElementSibling;
    feedback.style.display = 'block';
    // NEW: Auto-scroll on mobile
    setTimeout(() => {
      if (window.innerWidth <= 650) {
        feedback.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }, 100);
    if (isCorrect) {
      feedback.innerHTML = `✅ <strong>TEPAT SEKALI!</strong><br>${explanation}`;
      feedback.style.backgroundColor = "#27c881";
      feedback.style.color = "#1A1A1A";
      btn.disabled = true;
      btn.style.opacity = '0.5';
      const parenInput = document.getElementById('paren-input');
      if (parenInput) parenInput.disabled = true;
      revealQuizNext();
    } else {
      feedback.innerHTML = `❌ <strong>KODE BELUM TEPAT!</strong><br>Pastikan kamu menggabungkan 'is_admin or is_premium' di dalam tanda kurung (), lalu gunakan 'and password_ok'.`;
      feedback.style.backgroundColor = "#ff5c8a";
      feedback.style.color = "white";
      registerFailedInputAttempt(btn, feedback);
    }
  };

  window.checkAndGuess = function(userVal, btn, explanation) {
    const qid = currentQuestion.value?.qid;
    let normalizedUser = userVal.replace(/\s+/g, '').toLowerCase();
    const isCorrect = (normalizedUser === 'andaktif_organisasi==true' || normalizedUser === 'andaktif_organisasi' || normalizedUser === 'and(aktif_organisasi==true)');
    trackAttempt(qid, userVal, isCorrect);

    const container = btn.parentElement;
    const feedback = container.nextElementSibling;
    feedback.style.display = 'block';
    // NEW: Auto-scroll on mobile
    setTimeout(() => {
      if (window.innerWidth <= 650) {
        feedback.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }, 100);
    if (isCorrect) {
      feedback.innerHTML = `✅ <strong>TEPAT SEKALI!</strong><br>${explanation}`;
      feedback.style.backgroundColor = "#27c881";
      feedback.style.color = "#1A1A1A";
      btn.disabled = true;
      btn.style.opacity = '0.5';
      const andInput = document.getElementById('and-input');
      if (andInput) andInput.disabled = true;
      revealQuizNext();
    } else {
      feedback.innerHTML = `❌ <strong>KODE BELUM TEPAT!</strong><br>Coba lagi! Kamu butuh operator logika 'and' diikuti dengan kondisi pengecekan variabel aktif_organisasi.`;
      feedback.style.backgroundColor = "#ff5c8a";
      feedback.style.color = "white";
      registerFailedInputAttempt(btn, feedback);
    }
  };

  window.checkOrGuess = function(userVal, btn, explanation) {
    const qid = currentQuestion.value?.qid;
    let normalizedUser = userVal.replace(/\s+/g, '').toLowerCase();
    const isCorrect = (normalizedUser === 'orada_kupon==true' || normalizedUser === 'orada_kupon' || normalizedUser === 'or(ada_kupon==true)');
    trackAttempt(qid, userVal, isCorrect);

    const container = btn.parentElement;
    const feedback = container.nextElementSibling;
    feedback.style.display = 'block';
    // NEW: Auto-scroll on mobile
    setTimeout(() => {
      if (window.innerWidth <= 650) {
        feedback.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }, 100);
    if (isCorrect) {
      feedback.innerHTML = `✅ <strong>TEPAT SEKALI!</strong><br>${explanation}`;
      feedback.style.backgroundColor = "#27c881";
      feedback.style.color = "#1A1A1A";
      btn.disabled = true;
      btn.style.opacity = '0.5';
      const orInput = document.getElementById('or-input');
      if (orInput) orInput.disabled = true;
      revealQuizNext();
    } else {
      feedback.innerHTML = `❌ <strong>KODE BELUM TEPAT!</strong><br>Coba lagi! Kamu butuh operator logika 'or' diikuti dengan kondisi pengecekan variabel ada_kupon.`;
      feedback.style.backgroundColor = "#ff5c8a";
      feedback.style.color = "white";
      registerFailedInputAttempt(btn, feedback);
    }
  };

  window.checkNestedToLogicalGuess = function(userVal, btn, explanation) {
    const qid = currentQuestion.value?.qid;
    let normalizedUser = userVal.replace(/\s+/g, '').toLowerCase();
    const isCorrect = (normalizedUser === 'andcuaca=="cerah"' || normalizedUser === 'and(cuaca=="cerah")' || normalizedUser === 'andcuaca==\'cerah\'');
    trackAttempt(qid, userVal, isCorrect);

    const container = btn.parentElement;
    const feedback = container.nextElementSibling;
    
    feedback.style.display = 'block';
    // NEW: Auto-scroll on mobile
    setTimeout(() => {
      if (window.innerWidth <= 650) {
        feedback.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }, 100);
    if (isCorrect) {
      feedback.innerHTML = `✅ <strong>TEPAT SEKALI!</strong><br>${explanation}`;
      feedback.style.backgroundColor = "#27c881";
      feedback.style.color = "#1A1A1A";
      btn.disabled = true;
      btn.style.opacity = '0.5';
      const logicalInput = document.getElementById('logical-input');
      if (logicalInput) logicalInput.disabled = true;
      revealQuizNext();
    } else {
      feedback.innerHTML = `❌ <strong>KODE BELUM TEPAT!</strong><br>Pastikan kamu menggunakan operator 'and' lalu cek apakah 'cuaca == "cerah"'.`;
      feedback.style.backgroundColor = "#ff5c8a";
      feedback.style.color = "white";
      registerFailedInputAttempt(btn, feedback);
    }
  };

  window.checkNeedsWantsGuess = function(inputClass, btn) {
    const qid = currentQuestion.value?.qid;
    const inputs = document.querySelectorAll('.' + inputClass);
    let allFilled = true;
    let vals = [];
    inputs.forEach(input => {
      if (!input.value.trim()) allFilled = false;
      else vals.push(input.value.trim());
    });
    
    const container = btn.parentElement;
    const feedback = container.nextElementSibling;
    
    if (!allFilled) {
      feedback.style.display = 'block';
      setTimeout(() => {
        if (window.innerWidth <= 650) {
          feedback.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      }, 100);
      feedback.innerHTML = `❌ Lengkapi kelima contohnya terlebih dahulu ya!`;
      feedback.style.backgroundColor = "#ff5c8a";
      feedback.style.color = "white";
      registerFailedInputAttempt(btn, feedback);
      return;
    }
    
    trackAttempt(qid, vals.join(', '), true);

    btn.disabled = true;
    btn.style.opacity = '0.5';
    
    feedback.style.display = 'block';
    // NEW: Auto-scroll on mobile
    setTimeout(() => {
      if (window.innerWidth <= 650) {
        feedback.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }, 100);
    feedback.innerHTML = `✅ <strong>Tersimpan!</strong><br>Terima kasih sudah membagikan pemikiranmu.`;
    feedback.style.backgroundColor = "#27c881";
    feedback.style.color = "var(--black)";
    revealQuizNext();
  };

  window.checkIde6Guess = function(btn) {
    const qid = currentQuestion.value?.qid;
    const codeEl = document.getElementById('python-ide-6');
    const code = codeEl ? codeEl.value.toLowerCase() : '';
    trackAttempt(qid, code, true);
    const keywords = ['buku tulis', 'air minum', 'skin game', 'snack tambahan', 'pulsa', 'gantungan kunci'];
    let matchCount = 0;
    
    keywords.forEach(kw => {
      if (code.includes(kw)) matchCount++;
    });

    const container = btn.parentElement;
    const feedback = container.nextElementSibling.nextElementSibling;
    
    feedback.style.display = 'block';
    // NEW: Auto-scroll on mobile
    setTimeout(() => {
      if (window.innerWidth <= 650) {
        feedback.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }, 100);
    if (matchCount >= 3) {
      feedback.innerHTML = `✅ <strong>Bagus!</strong> Kamu sudah memakai setidaknya 3 barang dari tabel.`;
      feedback.style.backgroundColor = "#27c881";
      feedback.style.color = "var(--black)";
      btn.disabled = true;
      btn.style.opacity = '0.5';
      revealQuizNext();
    } else {
      feedback.innerHTML = `❌ Kamu baru memasukkan ${matchCount} barang dari tabel di kodemu. Minimal butuh 3 barang (misal: "Buku tulis", "Skin game", dsb).`;
      feedback.style.backgroundColor = "#ff5c8a";
      feedback.style.color = "white";
      registerFailedInputAttempt(btn, feedback);
    }
  };

  window.runPyodideCode = runPyodideCode;
  let finalProjectAttempts = 0;
  window.runAssignmentCode = function() {
    finalProjectAttempts++;
    studentProgress.value['Final_Project_Attempts'] = finalProjectAttempts;
    saveProgress('Final_Project_Attempts', finalProjectAttempts);
    runPyodideCode('python-ide-7', 'ide-output-7');
  };
  window.submitAssignmentCode = function() {
    const codeEl = document.getElementById('python-ide-7');
    const code = codeEl ? codeEl.value : '';
    let score = 'Submit';
    if (code.includes('if ') && code.includes('else:')) score = 'Bagus';
    
    studentProgress.value['Final_Project_Code'] = code;
    studentProgress.value['Final_Project_Score'] = score;
    saveProgress('Final_Project_Code', code);
    saveProgress('Final_Project_Score', score);

    showDashboardNotice({
      type: 'success',
      title: 'Tugas tersimpan',
      message: 'Progress kamu otomatis tersimpan di server. Selamat, kamu telah menyelesaikan Misi Conditional.'
    });
  };
};

onMounted(() => {
  quizObj.onValuesChange((values) => {
    quizModalStyles.value = {
      transform: `translateY(${values.y}px) scale(${values.scale})`,
      opacity: values.opacity
    };
  });

  if (window.YT && typeof window.YT.Player === "function") {
    youtubeReady.value = true;
    initializeYouTubePlayer(currentStep.value);
  } else {
    const oldReady = window.onYouTubeIframeAPIReady;
    window.onYouTubeIframeAPIReady = () => {
      if (oldReady) oldReady();
      youtubeReady.value = true;
      initializeYouTubePlayer(currentStep.value);
    };
  }
  exposeGlobalMethods();
});

watch(currentStep, (newStep) => {
  Object.keys(players).forEach(id => {
    if (Number(id) !== newStep && players[id] && typeof players[id].pauseVideo === 'function') {
      players[id].pauseVideo();
    }
  });

  if (quizState.value.activeQuizStep !== null && quizState.value.activeQuizStep !== newStep) {
    quizState.value.replayingQuizVideo = false;
    quizState.value.replayCheckpointArmed = false;
    quizReturn.value.isVisible = false;
  }

  nextTick(() => {
    initializeYouTubePlayer(newStep);
  });
});

const openQuizButtonHandler = () => {
  if (players[currentStep.value] && typeof players[currentStep.value].pauseVideo === "function") {
    players[currentStep.value].pauseVideo();
  }
  openQuiz(courseData[2].quizzes[0].questions, false);
};

const getStepQuizProgress = (stepId) => {
  const requiredQuizzes = (courseData[stepId]?.quizzes || [])
    .map((quiz) => {
      const requiredQuestions = (quiz.questions || []).filter(q => q.qid && q.type !== 'info' && q.continueOnly !== true);
      const isCompleted = requiredQuestions.length === 0 || requiredQuestions.every(q => {
        const ans = studentProgress.value[`${q.qid}_Ans`];
        return ans !== undefined && ans !== null && ans !== '';
      });
      const isActive = quizState.value.isOpen &&
        Number(quizState.value.activeQuizStep) === Number(stepId) &&
        quiz === quizState.value.activeQuizConfig;
      const hasOpenedThisSession = quiz.shown === true || isActive;
      return { quiz, requiredQuestions, isCompleted, isActive, hasOpenedThisSession };
    })
    .filter(item => item.requiredQuestions.length > 0);

  const total = requiredQuizzes.length;
  const recordedCompletedCount = requiredQuizzes.filter(item => item.isCompleted).length;
  const sessionCompletedCount = requiredQuizzes.filter(item => item.isCompleted && item.hasOpenedThisSession).length;
  const openedCount = requiredQuizzes.filter(item => item.hasOpenedThisSession).length;
  const activeQuizIndex = requiredQuizzes.findIndex(item => item.isActive) + 1;
  const displayCompletedCount = sessionCompletedCount;

  return { requiredQuizzes, total, recordedCompletedCount, displayCompletedCount, openedCount, activeQuizIndex };
};

const isStepFinished = (stepId) => {
  let videoWatched = true;
  if (courseData[stepId]?.videoId) {
    videoWatched = !!videoWatchedStatus.value[stepId];
  }

  const quizProgress = getStepQuizProgress(stepId);
  const allQuizzesCompleted = quizProgress.requiredQuizzes.every(item => item.isCompleted);
  
  let projectSubmitted = true;
  if (stepId === 2) {
    const projCol = 'Project1_Code';
    projectSubmitted = !!studentProgress.value[projCol];
  } else if (stepId === 7) {
    const obsCol = 'Idea_Obs';
    const solCol = 'Idea_Sol';
    const uiCol = 'Idea_UI_Code';
    projectSubmitted = !!(studentProgress.value[obsCol] && studentProgress.value[solCol] && studentProgress.value[uiCol]);
  }
  
  console.log(`[Step ${stepId} Debug] Video Watched: ${videoWatched}, Quizzes Completed: ${quizProgress.recordedCompletedCount} / ${quizProgress.total}, Project Submitted: ${projectSubmitted}`);
  
  return videoWatched && allQuizzesCompleted && projectSubmitted;
};

const getStepBlockingNotice = (stepId, targetStep = null) => {
  const stepConfig = courseData[stepId] || {};
  const moduleLabel = `Modul ${stepId}`;
  const quizProgress = getStepQuizProgress(stepId);
  const destinationLabel = targetStep ? `Modul ${targetStep}` : 'modul berikutnya';
  const playerState = playerStates.value[stepId] || {};
  const videoStarted = Boolean(
    videoWatchedStatus.value[stepId] ||
    playerState.hasStarted ||
    playerState.currentTime > 0 ||
    quizProgress.openedCount > 0
  );

  if (stepConfig.videoId && !videoStarted) {
    return {
      type: 'warning',
      title: `Mulai ${moduleLabel} dulu ya!`,
      message: `${destinationLabel} masih terkunci karena kamu belum mulai menonton video ${moduleLabel}.\n\nYuk mulai dari langkah pertama:\n\n1. Tonton video ${moduleLabel} sampai selesai.\n2. Setelah video selesai, kerjakan Quiz/Checkpoint ${moduleLabel}.\n3. Jika semua checkpoint sudah selesai, ${destinationLabel} akan terbuka otomatis.`,
      actionLabel: `Mulai ${moduleLabel}`,
      actionStep: Number(stepId)
    };
  }

  let projectSubmitted = true;
  if (stepId === 5) {
    // TODO: Buka komentar ini saat akan push ke Git agar kewajiban upload aktif
    const projCol = 'Project1_Code';
    projectSubmitted = !!studentProgress.value[projCol];
  }

  let statusText = '';
  if (!videoWatchedStatus.value[stepId]) {
    statusText = 'videonya belum selesai ditonton (minimal 90-95%)';
  } else if (!projectSubmitted) {
    statusText = 'kamu belum mengumpulkan form project (link atau file .aia)';
  } else {
    statusText = 'ada quiz/checkpoint yang belum tuntas dikerjakan';
  }

  const progressText = quizProgress.total > 0 
    ? `\n\nProgress Checkpoint Modul ${stepId}: ${quizProgress.recordedCompletedCount} / ${quizProgress.total} selesai.`
    : '';

  return {
    type: 'warning',
    title: `${moduleLabel} belum selesai`,
    message: `Kamu sudah mulai belajar, tapi ${statusText}.\n\nPastikan syarat di atas sudah terpenuhi sebelum ${destinationLabel} terbuka otomatis.${progressText}`,
    actionLabel: `Lanjutkan ${moduleLabel}`,
    actionStep: Number(stepId)
  };
};

const goToStep = (step) => {
  if (step <= currentStep.value) {
    currentStep.value = step;
    return;
  }
  for (let i = 1; i < step; i++) {
    if (!isStepFinished(i)) {
      showDashboardNotice(getStepBlockingNotice(i, step));
      return;
    }
  }
  currentStep.value = step;
};

const handleStepSelect = (event) => {
  const requestedStep = Number(event.target.value);
  goToStep(requestedStep);
  event.target.value = String(currentStep.value);
};

const prevStep = () => {
  if (currentStep.value > 1) {
    currentStep.value--;
  }
};

const nextStep = () => {
  if (!isStepFinished(currentStep.value)) {
    showDashboardNotice(getStepBlockingNotice(currentStep.value, currentStep.value + 1));
    return;
  }
  if (currentStep.value < Object.keys(courseData).length) {
    const previousStep = currentStep.value;
    currentStep.value++;
    console.log(`[DEBUG] Tab berpindah dari Materi ${previousStep} ke Materi ${currentStep.value}.`);
  }
};

const getStepConfig = (stepId) => {
  return courseData[stepId];
};
</script>

<template>
  <img class="planet planet-one" src="https://cdn-web-2.ruangguru.com/landing-pages/assets/e49806a2-dcc4-4858-a261-c4e33b798180.png" alt="">
  <img class="planet planet-two" src="https://cdn-web-2.ruangguru.com/landing-pages/assets/eaa66ac5-e69c-46f2-b942-909bcaad579a.png" alt="">

  <transition name="fade">
    <div v-if="!isLoggedIn" class="login-overlay">
      <div class="login-card">
        <div class="login-copy">
          <div class="brand-group-login">
            <img class="rg-logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Ruangguru_logo.svg/3840px-Ruangguru_logo.svg.png" alt="Ruangguru">
            <img class="uob-logo" src="https://cdn-web-2.ruangguru.com/landing-pages/assets/37185db7-24a8-467d-aabb-1d5df48f9bc0.png" alt="UOB">
          </div>
          <span class="login-kicker">UOB My Digital Space</span>
          <h1>App Inventor Learning Dashboard</h1>
          <p>Masuk dengan email siswa untuk membuka materi kelasmu.</p>
          <div class="login-highlights" aria-label="Fitur pembelajaran">
            <span>Middle School</span>
            <span>App Inventor</span>
            <span>Async Class</span>
          </div>
        </div>

        <div class="login-form-panel">
          <span class="login-step">Materi Grup B - SMP</span>
          <h2>Masuk ke kelas</h2>
          <div class="input-group">
            <label for="login-school-a">Nama sekolah</label>
            <div class="login-combobox">
              <input id="login-school-a" type="text" v-model="loginSchool" placeholder="Cari nama sekolah" autocomplete="off" @focus="openSchoolDropdown" @blur="closeSchoolDropdownSoon" @input="handleSchoolInput" :disabled="isLoggingIn">
              <div v-if="isSchoolDropdownOpen" class="login-dropdown">
                <template v-if="!isSchoolLoading">
                  <button v-for="school in schoolOptions" :key="school" type="button" @mousedown.prevent="selectSchool(school)">
                    {{ school }}
                  </button>
                </template>
                <p v-if="isSchoolLoading">Memuat data sekolah...</p>
                <p v-else-if="!schoolOptions.length">Sekolah tidak ditemukan.</p>
              </div>
            </div>

            <label for="login-email-a">Email terdaftar di Akademia Ruangguru</label>
            <input id="login-email-a" type="email" v-model="loginEmail" placeholder="nama@email.com" @input="handleEmailInput" @keyup.enter="handleLogin" :disabled="isLoggingIn || !selectedSchool">

            <button type="button" class="login-help-toggle" @click="toggleEmailHelp" :disabled="!selectedSchool">
              Tidak yakin emailnya? Cari bantuan lewat nama/email
            </button>

            <div v-if="emailHelpOpen" class="email-help-panel">
              <label for="login-help-a">Cari nama siswa/orang tua atau email</label>
              <input id="login-help-a" type="text" v-model="emailHelpQuery" placeholder="Contoh: Taylor atau gmail" @input="handleEmailHelpInput">
              <div class="email-help-results">
                <p v-if="!emailHelpQuery.trim()">Ketik nama atau sebagian email yang mungkin terdaftar.</p>
                <p v-else-if="isEmailHelpLoading">Mencari data...</p>
                <p v-else-if="!emailHelpResults.length">Belum ada data yang mirip di sekolah ini.</p>
                <div v-for="student in emailHelpResults" :key="`${student.school}-${student.name}-${student.maskedEmail}`" class="email-help-result">
                  <strong>{{ student.name }}</strong>
                  <span class="email-help-label">Email terdaftar:</span>
                  <code v-if="student.maskedEmail">{{ student.maskedEmail }}</code>
                  <span v-else class="email-help-missing">Email belum tersedia. Coba cek lagi email yang didaftarkan di Akademia Ruangguru.</span>
                </div>
                <p v-if="emailHelpResults.length" class="email-help-note">Gunakan email terdaftar di atas untuk masuk ke kelas.</p>
              </div>
            </div>

            <button @click="handleLogin" :disabled="isLoggingIn || !selectedSchool || !loginEmail.trim()" class="login-btn">
              {{ isLoggingIn ? 'Memuat...' : 'Mulai Belajar' }}
            </button>
          </div>
          <p class="login-helper">Gunakan email pribadi yang sudah didaftarkan di Akademia Ruangguru.</p>

          <transition name="pop">
            <div v-if="showLoginError" class="login-error-msg">
              <span class="icon">!</span>
              <div>
                <strong>{{ loginErrorTitle }}</strong>
                <p>{{ loginErrorMessage }}</p>
                <div v-if="loginEmailSuggestion" class="registered-email-card">
                  <span>Email terdaftar di sekolah ini:</span>
                  <strong>{{ loginEmailSuggestion.maskedEmail || 'Email belum tersedia' }}</strong>
                  <p>Coba cek lagi tanda titik, huruf yang tertukar, atau domain emailnya.</p>
                </div>
              </div>
            </div>
          </transition>
        </div>
      </div>
    </div>
  </transition>

  <div class="site-shell" v-show="isLoggedIn">
    <header class="topbar">
      <div class="brand-group">
        <img class="rg-logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Ruangguru_logo.svg/3840px-Ruangguru_logo.svg.png" alt="Ruangguru">
        <img class="uob-logo" src="https://cdn-web-2.ruangguru.com/landing-pages/assets/37185db7-24a8-467d-aabb-1d5df48f9bc0.png" alt="UOB">
      </div>
      <div class="student-chip" aria-label="Profil siswa" @click="showProfileMenu = !showProfileMenu">
        <div class="avatar" aria-hidden="true"></div>
        <div class="student-info">
          <strong>
            {{ studentData.name || 'Siswa Kalananti' }}
            <span class="dropdown-icon">▼</span>
          </strong>
          <span v-if="studentData.school">{{ studentData.school }}</span>
          <span v-else>Siap lanjut belajar</span>
        </div>
        
        <transition name="fade">
          <div v-if="showProfileMenu" class="profile-dropdown">
            <button @click.stop="handleLogout" class="dropdown-item">⏏ Keluar</button>
          </div>
        </transition>
      </div>
    </header>

    <main class="dashboard">
      <aside class="sidebar">
        <div class="eyebrow">Asynchronous Learning</div>
        <h1>Misi: Kuasai Conditional</h1>
        <p class="sidebar-intro">
          Pelajari cara program mengambil keputusan dengan <strong>if</strong>, <strong>else</strong>, dan <strong>elif</strong>.
        </p>

        <div class="mission-progress" aria-label="Progres pembelajaran">
          <div class="progress-copy">
            <span>Progres misi</span>
            <span id="progressText">{{ currentStep }} dari {{ totalSteps }}</span>
          </div>
          <div class="progress-track">
            <div class="progress-fill" :style="{ width: (currentStep / totalSteps * 100) + '%' }"></div>
          </div>
        </div>

        <nav class="mobile-nav">
          <label for="mobile-lesson-select">Pilih Modul</label>
          <div class="select-wrapper">
            <select id="mobile-lesson-select" :value="currentStep" @change="handleStepSelect">
              <option v-for="(data, step) in courseData" :key="step" :value="parseInt(step)">
                0{{ step }} {{ data.title }}
              </option>
            </select>
          </div>
        </nav>

        <nav class="lesson-nav" aria-label="Daftar video">
          <button class="lesson-tab" v-for="(data, step) in courseData" :key="step" :class="{ active: currentStep === parseInt(step) }" type="button" @click="goToStep(parseInt(step))">
            <span class="tab-number">0{{ step }}</span>
            <span class="tab-copy">
              <strong>{{ data.title }}</strong>
              <span>{{ data.duration }}</span>
            </span>
            <span class="tab-arrow" aria-hidden="true">›</span>
          </button>
        </nav>

        <div class="help-card">
          Ada bagian yang masih membingungkan?
          <a href="mailto:fasilitator@kalananti.id">Tanya fasilitator</a>
        </div>
      </aside>

      <section class="content">
        <div class="content-top">
          <div>
            <p class="lesson-kicker">{{ courseData[currentStep].kicker }}</p>
            <h2 class="lesson-title">{{ courseData[currentStep].title }}</h2>
          </div>
          <span class="duration-pill">{{ courseData[currentStep].duration }}</span>
        </div>

        <section class="step-panel" v-for="(data, step) in courseData" :key="step" :id="'step-' + step" v-show="currentStep === parseInt(step)">
          <div class="video-frame" :class="{ 'player-ready': playerStates[step]?.isReady }" :data-video-step="step">
            <div :id="'youtube-player-' + step"></div>
            <div class="custom-thumbnail" v-show="!playerStates[step]?.hasStarted" @click="togglePlay(step)">
              <img :src="data.thumbnail || 'https://cdn-web-2.ruangguru.com/landing-pages/assets/fec32e8d-d711-48a2-bd22-59581f0594c1.jpg'" alt="Thumbnail" />
            </div>
            <button class="video-center-play" type="button" v-show="!playerStates[step]?.isPlaying && !playerStates[step]?.isBuffering && (playerStates[step]?.isReady || !playerStates[step]?.hasStarted)" @click="togglePlay(step)">▶</button>
            <div class="video-loading-overlay" v-show="playerStates[step]?.isBuffering || (playerStates[step]?.hasStarted && !playerStates[step]?.isReady)">
              <div class="spinner"></div>
            </div>
            <div class="video-controls" :aria-label="'Kontrol video ' + step" v-show="!playerStates[step]?.introPlaying">
              <button class="video-control-button video-play" type="button" @click="togglePlay(step)">{{ playerStates[step]?.isPlaying ? "⏸" : "▶" }}</button>
              <input class="video-seek" type="range" min="0" max="100" step="0.1" :value="playerStates[step]?.progress || 0" @input="onSeekInput(step, $event)" aria-label="Posisi video">
              <span class="video-time">{{ playerStates[step]?.currentTimeFormatted || "0:00" }} / {{ playerStates[step]?.durationFormatted || "0:00" }}</span>
              <button class="video-control-button video-mute" type="button" @click="toggleMute(step)">{{ playerStates[step]?.isMuted ? "🔇" : "🔊" }}</button>
              <button class="video-control-button video-fullscreen" type="button" @click="toggleFullscreen(step)">⛶</button>
            </div>
          </div>

          <div class="bookmarks-container" v-if="data.bookmarks?.length > 0">
            <button class="bookmark-btn" v-for="bm in data.bookmarks" :key="bm.label" @click="seekToBookmark(step, bm.time)">
              <span class="bookmark-time">{{ formatVideoTime(bm.time) }}</span> {{ bm.label }}
            </button>
          </div>

          <div class="reading-container" v-if="data.summaryHtml">
            <details class="lesson-reading-accordion" :open="isDesktop ? true : undefined">
              <summary>Buka Materi Bacaan</summary>
              <div class="lesson-reading" v-html="data.summaryHtml"></div>
              
              <!-- Project Upload Area (Integrated into Reading Material) -->
              <div v-if="currentStep === 2" class="project-upload-area" style="background: var(--paper); border-radius: 16px; padding: 32px; margin-top: 32px; border: 2px dashed var(--line); text-align: center; box-shadow: var(--shadow);">
                <h3 style="margin-top: 0; color: var(--navy); font-size: 1.5rem; font-weight: 800; letter-spacing: -0.02em;">Kumpulkan Mini Project</h3>
                <p style="color: var(--muted); margin-bottom: 24px; font-size: 1.05rem;">Pilih metode untuk mengumpulkan kreasi aplikasi MIT App Inventor milikmu.</p>
                
                <div style="display: flex; gap: 16px; margin-bottom: 32px; justify-content: center;">
                  <label :style="{ border: projectUploadType === 'link' ? '2px solid var(--blue)' : '2px solid var(--line)', backgroundColor: projectUploadType === 'link' ? 'var(--soft-blue)' : 'var(--paper)', cursor: 'pointer', padding: '16px 24px', borderRadius: '12px', flex: 1, transition: 'all 0.2s ease', position: 'relative' }">
                    <input type="radio" v-model="projectUploadType" value="link" name="uploadType" style="position: absolute; opacity: 0;">
                    <div style="font-weight: 700; color: var(--navy); margin-bottom: 4px;">🔗 Link Galeri</div>
                    <div style="font-size: 0.85rem; color: var(--muted);">Paste link dari Galeri</div>
                  </label>
                  <label :style="{ border: projectUploadType === 'file' ? '2px solid var(--blue)' : '2px solid var(--line)', backgroundColor: projectUploadType === 'file' ? 'var(--soft-blue)' : 'var(--paper)', cursor: 'pointer', padding: '16px 24px', borderRadius: '12px', flex: 1, transition: 'all 0.2s ease', position: 'relative' }">
                    <input type="radio" v-model="projectUploadType" value="file" name="uploadType" style="position: absolute; opacity: 0;">
                    <div style="font-weight: 700; color: var(--navy); margin-bottom: 4px;">📁 Upload File</div>
                    <div style="font-size: 0.85rem; color: var(--muted);">Pilih file berformat .aia</div>
                  </label>
                </div>

                <div v-if="projectUploadType === 'link'" style="margin-bottom: 24px; text-align: left;">
                  <label style="display: block; font-weight: 600; margin-bottom: 8px; color: var(--ink);">Masukkan Link Galeri MIT App Inventor</label>
                  <input type="text" v-model="projectLink" placeholder="Contoh: https://gallery.appinventor.mit.edu/?galleryid=..." style="width: 100%; padding: 16px; border: 2px solid var(--line); border-radius: 12px; font-family: inherit; font-size: 1rem; transition: border-color 0.2s;" onfocus="this.style.borderColor='var(--blue)'" onblur="this.style.borderColor='var(--line)'">
                </div>

                <div v-if="projectUploadType === 'file'" style="margin-bottom: 24px; text-align: left;">
                  <label style="display: block; font-weight: 600; margin-bottom: 8px; color: var(--ink);">Pilih File Aplikasi (.aia)</label>
                  <div style="position: relative; overflow: hidden; display: inline-block; width: 100%;">
                    <button type="button" style="width: 100%; padding: 16px; border: 2px dashed var(--muted); border-radius: 12px; background: var(--soft-blue); color: var(--navy); font-weight: 600; cursor: pointer; transition: all 0.2s;">
                      {{ projectFile ? projectFile.name : 'Klik untuk mencari file .aia di komputermu' }}
                    </button>
                    <input type="file" accept=".aia" @change="handleProjectFileChange" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0; cursor: pointer;">
                  </div>
                </div>

                <button @click="submitProject" :disabled="isUploading" style="background: var(--blue); color: white; padding: 16px 32px; border: none; border-radius: 99px; font-weight: 700; font-size: 1.1rem; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 12px; transition: all 0.2s; box-shadow: 0 4px 12px rgba(11, 120, 246, 0.3);" :style="{ opacity: isUploading ? 0.7 : 1, transform: isUploading ? 'scale(0.98)' : 'scale(1)' }">
                  <span v-if="isUploading" class="spinner" style="width: 20px; height: 20px; border-width: 3px; border-top-color: white;"></span>
                  {{ isUploading ? 'Sedang Mengirim...' : 'Kumpulkan Sekarang' }}
                </button>

                <div v-if="projectUploadMessage" :style="{ marginTop: '24px', padding: '16px', borderRadius: '12px', fontSize: '0.95rem', fontWeight: '500', backgroundColor: projectUploadStatus === 'error' ? '#FEF2F2' : '#F0FDF4', color: projectUploadStatus === 'error' ? '#B91C1C' : '#15803D', border: '1px solid', borderColor: projectUploadStatus === 'error' ? '#FCA5A5' : '#BBF7D0' }">
                  {{ projectUploadMessage }}
                </div>
                
                <div style="margin-top: 32px; padding-top: 24px; border-top: 1px solid var(--line); text-align: center;">
                  <p style="margin: 0; font-size: 0.9rem; color: var(--muted);">Butuh bantuan cara submit tugas?</p>
                  <a href="https://youtu.be/TfUGR1dKGa8?si=NRLWkXvCHbWa4BsW" target="_blank" style="display: inline-flex; align-items: center; gap: 6px; color: var(--blue); text-decoration: none; font-weight: 700; font-size: 0.95rem; margin-top: 8px;">
                    ▶ Tonton Tutorial Singkat
                  </a>
                </div>
              </div>

              <!-- Idea Brainstorming Area (Tab 7) -->
              <div v-if="currentStep === 7" class="idea-brainstorm-area" style="background: var(--paper); border-radius: 16px; padding: 32px; margin-top: 32px; border: 2px dashed var(--line); text-align: left; box-shadow: var(--shadow);">
                <h3 style="margin-top: 0; color: var(--navy); font-size: 1.5rem; font-weight: 800; letter-spacing: -0.02em; text-align: center;">Misi Brainstorming Ide Aplikasi! 🚀</h3>
                <p style="color: var(--muted); margin-bottom: 24px; font-size: 1.05rem; text-align: center;">Lengkapi kotak di bawah ini dan unggah desain aplikasimu.</p>
                
                <div style="margin-bottom: 24px;">
                  <label style="display: block; font-weight: 700; margin-bottom: 8px; color: var(--ink);">Text Box 1: Observasi Lingkungan</label>
                  <p style="font-size: 0.9rem; color: var(--muted); margin-top: 0; margin-bottom: 8px;">Coba perhatikan sekitarmu! Ceritakan 1 masalah nyata di sekolah, rumah, atau lingkungan bermainmu yang ingin sekali kamu selesaikan.</p>
                  <textarea v-model="ideaObs" placeholder="Misalnya: Teman-teman sering lupa jadwal piket, atau tanaman di rumah sering lupa disiram..." style="width: 100%; padding: 16px; border: 2px solid var(--line); border-radius: 12px; font-family: inherit; font-size: 1rem; min-height: 100px; resize: vertical; transition: border-color 0.2s;" onfocus="this.style.borderColor='var(--blue)'" onblur="this.style.borderColor='var(--line)'"></textarea>
                </div>

                <div style="margin-bottom: 24px;">
                  <label style="display: block; font-weight: 700; margin-bottom: 8px; color: var(--ink);">Text Box 2: Penemu Solusi Digital</label>
                  <p style="font-size: 0.9rem; color: var(--muted); margin-top: 0; margin-bottom: 8px;">Sekarang, bayangkan kamu adalah seorang pencipta aplikasi hebat! Apa NAMA aplikasimu dan BAGAIMANA caramu menggunakan aplikasi itu untuk memecahkan masalah tadi?</p>
                  <textarea v-model="ideaSol" placeholder="Nama aplikasiku adalah [Tulis Nama], aplikasi ini bisa menjadi solusi digital dengan cara..." style="width: 100%; padding: 16px; border: 2px solid var(--line); border-radius: 12px; font-family: inherit; font-size: 1rem; min-height: 100px; resize: vertical; transition: border-color 0.2s;" onfocus="this.style.borderColor='var(--blue)'" onblur="this.style.borderColor='var(--line)'"></textarea>
                </div>

                <div style="margin-bottom: 32px;">
                  <label style="display: block; font-weight: 700; margin-bottom: 8px; color: var(--ink);">Text Box 3: Gambarkan Tampilan Aplikasimu (UI Designer)</label>
                  <p style="font-size: 0.9rem; color: var(--muted); margin-top: 0; margin-bottom: 8px;">Buat gambar di kertas, Figma, atau Canva. Bayangkan layar utama aplikasimu sudah jadi, kira-kira ada tombol apa saja di sana? Tulisan atau petunjuk apa yang akan dibaca oleh pengguna? Upload foto/desain (JPG/PNG) ke sini.</p>
                  <div style="position: relative; overflow: hidden; display: inline-block; width: 100%;">
                    <button type="button" style="width: 100%; padding: 16px; border: 2px dashed var(--muted); border-radius: 12px; background: var(--soft-blue); color: var(--navy); font-weight: 600; cursor: pointer; transition: all 0.2s;">
                      {{ ideaUIFile ? ideaUIFile.name : 'Klik untuk mengunggah gambar JPG/PNG' }}
                    </button>
                    <input type="file" accept="image/png, image/jpeg, image/jpg" @change="handleIdeaUIFileChange" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; opacity: 0; cursor: pointer;">
                  </div>
                </div>

                <div style="text-align: center;">
                  <button @click="submitIdea" :disabled="isUploadingIdea" style="background: var(--blue); color: white; padding: 16px 32px; border: none; border-radius: 99px; font-weight: 700; font-size: 1.1rem; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 12px; transition: all 0.2s; box-shadow: 0 4px 12px rgba(11, 120, 246, 0.3);" :style="{ opacity: isUploadingIdea ? 0.7 : 1, transform: isUploadingIdea ? 'scale(0.98)' : 'scale(1)' }">
                    <span v-if="isUploadingIdea" class="spinner" style="width: 20px; height: 20px; border-width: 3px; border-top-color: white;"></span>
                    {{ isUploadingIdea ? 'Sedang Mengirim...' : 'Kirim Ide Brilianmu!' }}
                  </button>

                  <div v-if="ideaUploadMessage" :style="{ marginTop: '24px', padding: '16px', borderRadius: '12px', fontSize: '0.95rem', fontWeight: '500', backgroundColor: ideaUploadStatus === 'error' ? '#FEF2F2' : '#F0FDF4', color: ideaUploadStatus === 'error' ? '#B91C1C' : '#15803D', border: '1px solid', borderColor: ideaUploadStatus === 'error' ? '#FCA5A5' : '#BBF7D0' }">
                    {{ ideaUploadMessage }}
                  </div>
                </div>
              </div>
            </details>
          </div>
        </section>
        
        <div class="nav-buttons">
          <button class="nav-button secondary" type="button" :disabled="currentStep === 1" @click="prevStep()">
            ← Modul Sebelumnya
          </button>
          <button class="nav-button primary" type="button" :disabled="currentStep === Object.keys(courseData).length" @click="nextStep()">
            Modul Berikutnya →
          </button>
        </div>
      </section>
    </main>

    <footer class="footer-note">
      Copyright © 2025 PT Ruang Raya Indonesia. Materi tidak boleh disebarluaskan tanpa izin.
    </footer>
  </div>

  
  <div class="quiz-overlay" id="quizOverlay" role="dialog" aria-modal="true" aria-labelledby="quizTitle" :class="{ open: quizState.isOpen }">
    <div class="quiz-dialog">
      <header class="quiz-header">
        <span class="quiz-header-icon" aria-hidden="true">?</span>
        <div>
          <p class="quiz-kicker">Checkpoint pemahaman</p>
          <h2 id="quizTitle">Mini Quiz Waktu!</h2>
          <p class="quiz-subtitle">Jawab berdasarkan materi yang baru kamu tonton.</p>
        </div>
      </header>
      <div class="quiz-body">
        <div class="quiz-progress" id="quizProgress" aria-label="Progres kuis">
          <span 
            v-for="(_, index) in quizState.shuffledQuestions" 
            :key="index" 
            class="quiz-dot"
            :class="{ 
              done: index < quizState.currentQuestionIdx, 
              active: index === quizState.currentQuestionIdx 
            }"
          ></span>
        </div>
        <div v-show="currentQuestion && !currentQuestion.html" class="quiz-question" id="quizQuestion" v-html="currentQuestion ? currentQuestion.question : 'Memuat pertanyaan...'">
        </div>
        <div v-if="currentQuestion && currentQuestion.html" id="quizCustomHtml" v-html="currentQuestion.html"></div>
        <div v-show="currentQuestion && !currentQuestion.html" class="answer-row" id="answerRow">
          <button 
            v-for="(choice, cIdx) in getQuestionChoices(currentQuestion)" 
            :key="cIdx" 
            class="answer-button"
            :class="{ 
              true: choice === 'TRUE' || choice === 'True',
              false: choice === 'FALSE' || choice === 'False'
            }"
            @click="handleStandardAnswer(choice)"
            :disabled="quizState.choicesDisabled"
            :style="{ opacity: quizState.choicesDisabled ? (quizState.selectedChoice === choice ? 1 : 0.5) : 1 }"
          >
            {{ choice }}
          </button>
        </div>
        <div class="quiz-feedback" id="quizFeedback" role="status" v-show="quizState.quizFeedback" :class="quizState.quizFeedbackType">
          <span v-html="quizState.quizFeedback"></span>
        </div>
        <div class="quiz-actions">
          <button class="quiz-review" type="button" @click="replayActiveQuizVideo">↺ Ulangi 30 detik video</button>
          <button class="quiz-next" type="button" v-show="quizState.isNextBtnVisible" @click="goToNextQuestion">{{ quizState.nextBtnText || (quizState.currentQuestionIdx < quizState.shuffledQuestions.length - 1 ? 'Soal berikutnya →' : 'Selesai →') }}</button>
        </div>
      </div>
    </div>
  </div>

  <div class="quiz-return" id="quizReturn" role="status" :class="{ visible: quizReturn.isVisible }">
    <p>Sudah cukup mengulang materinya? Kamu bisa kembali ke checkpoint kapan saja.</p>
    <button type="button" @click="returnToActiveQuiz">Kembali ke kuis sekarang →</button>
  </div>

  <div
    v-if="dashboardNotice.isOpen"
    class="dashboard-notice-backdrop"
    role="dialog"
    aria-modal="true"
    aria-labelledby="dashboardNoticeTitle"
    @click.self="closeDashboardNotice"
  >
    <section class="dashboard-notice-card" :class="dashboardNotice.type">
      <div class="dashboard-notice-icon" aria-hidden="true">{{ dashboardNoticeIcon }}</div>
      <div class="dashboard-notice-copy">
        <p class="dashboard-notice-kicker">Checkpoint belajar</p>
        <h3 id="dashboardNoticeTitle">{{ dashboardNotice.title }}</h3>
        <p class="dashboard-notice-message">{{ dashboardNotice.message }}</p>
      </div>
      <button type="button" class="dashboard-notice-action" @click="handleDashboardNoticeAction">
        {{ dashboardNotice.actionLabel }}
      </button>
    </section>
  </div>

  <div class="completion-toast" id="completionToast" role="status">
    Misi selesai. Kamu sudah mempelajari conditional, logical operator, dan penerapannya dalam perencanaan keuangan.
  </div>
</template>

<style>
.dashboard-notice-backdrop {
  position: fixed;
  inset: 0;
  z-index: 10000;
  display: grid;
  place-items: center;
  padding: 24px;
  background: rgba(26, 26, 26, 0.42);
  backdrop-filter: blur(6px);
}

.dashboard-notice-card {
  width: min(440px, 100%);
  display: grid;
  grid-template-columns: 56px 1fr;
  gap: 16px;
  align-items: start;
  padding: 22px;
  background: #fff7d8;
  border: 4px solid #1a1a1a;
  border-radius: 18px;
  box-shadow: 10px 10px 0 #1a1a1a;
  color: #1a1a1a;
  animation: dashboard-notice-in 180ms ease-out both;
}

.dashboard-notice-card.success {
  background: #dcffe9;
}

.dashboard-notice-icon {
  width: 52px;
  height: 52px;
  display: grid;
  place-items: center;
  border: 3px solid #1a1a1a;
  border-radius: 14px;
  background: #ffce4a;
  box-shadow: 4px 4px 0 #1a1a1a;
  font-weight: 900;
  font-size: 24px;
}

.dashboard-notice-message {
  white-space: pre-wrap;
}

.dashboard-notice-card.success .dashboard-notice-icon {
  background: #27c881;
}

.dashboard-notice-copy {
  min-width: 0;
}

.dashboard-notice-kicker {
  margin: 0 0 6px;
  font-size: 12px;
  font-weight: 900;
  letter-spacing: 0;
  text-transform: uppercase;
  color: #5b5b5b;
}

.dashboard-notice-copy h3 {
  margin: 0 0 8px;
  font-size: 24px;
  line-height: 1.05;
}

.dashboard-notice-copy p:last-child {
  margin: 0;
  font-size: 16px;
  line-height: 1.45;
  font-weight: 700;
}

.dashboard-notice-action {
  grid-column: 1 / -1;
  justify-self: end;
  min-width: 132px;
  padding: 12px 18px;
  border: 3px solid #1a1a1a;
  border-radius: 12px;
  background: #1f6bff;
  color: #ffffff;
  box-shadow: 4px 4px 0 #1a1a1a;
  font: inherit;
  font-weight: 900;
  cursor: pointer;
}

.dashboard-notice-action:hover {
  transform: translate(-1px, -1px);
  box-shadow: 5px 5px 0 #1a1a1a;
}

@keyframes dashboard-notice-in {
  from {
    opacity: 0;
    transform: translateY(14px) scale(0.97);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@media (max-width: 520px) {
  .dashboard-notice-card {
    grid-template-columns: 44px 1fr;
    gap: 12px;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 7px 7px 0 #1a1a1a;
  }

  .dashboard-notice-icon {
    width: 42px;
    height: 42px;
    border-radius: 11px;
    font-size: 19px;
  }

  .dashboard-notice-copy h3 {
    font-size: 21px;
  }

  .dashboard-notice-action {
    justify-self: stretch;
  }
}
</style>
