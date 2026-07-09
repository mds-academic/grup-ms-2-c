import os
import re

repos = [
    'sesi25-26/grup-hs-2-a',
    'sesi27-29/grup-hs-2-b',
    'sesi30-32/grup-hs-2-c',
    'sesi40-44/grup-hs-2-d'
]

notice_css = """
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
"""

notice_html = """
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
        <p>{{ dashboardNotice.message }}</p>
      </div>
      <button type="button" class="dashboard-notice-action" @click="closeDashboardNotice">
        {{ dashboardNotice.actionLabel }}
      </button>
    </section>
  </div>
"""

notice_js = """
const dashboardNotice = reactive({
  isOpen: false,
  type: 'warning',
  title: '',
  message: '',
  actionLabel: 'Mengerti'
});
const dashboardNoticeIcon = computed(() => ({
  success: 'OK',
  warning: '!',
  error: '!'
})[dashboardNotice.type] || '!');
const showDashboardNotice = ({ type = 'warning', title = 'Perhatian', message = '', actionLabel = 'Mengerti' } = {}) => {
  dashboardNotice.type = type;
  dashboardNotice.title = title;
  dashboardNotice.message = message;
  dashboardNotice.actionLabel = actionLabel;
  dashboardNotice.isOpen = true;
};
const closeDashboardNotice = () => {
  dashboardNotice.isOpen = false;
};
"""

print("Running script...")
