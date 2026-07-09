import asyncio
from playwright.async_api import async_playwright

urls = ["http://localhost:5174/"]

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        for url in urls:
            print(f"\\n{'='*50}\\nTesting URL: {url}\\n{'='*50}")
            page = await browser.new_page()
            try:
                await page.goto(url, wait_until='domcontentloaded', timeout=60000)
                
                # 1. Login normally (Simulate user typing and waiting for API)
                print("Logging in natively...")
                await page.fill('input[placeholder="Cari nama sekolah"]', 'SMA 1 New York')
                
                # Wait for dropdown items (up to 15 seconds because it's slow)
                try:
                    await page.wait_for_selector('.login-dropdown button', timeout=15000)
                    # Click the first matching item
                    await page.click('.login-dropdown button')
                except Exception:
                    print("Dropdown didn't appear in 15 seconds. Bug 2 confirmed!")
                    # We can't proceed natively if dropdown fails and disables email field
                    # We will try to type in email just in case the UI allows it
                    pass
                
                await page.fill('input[type="email"]', 'taylorswift@ruangguru.id')
                await page.click('button.login-btn')
                
                # Wait for tabs to appear
                await page.wait_for_selector('.lesson-tab', timeout=15000)
                print("Login successful natively!")
                
                # 2. Iterate through all tabs
                tabs_count = await page.locator('.lesson-tab').count()
                print(f"Found {tabs_count} tabs to process.")
                
                for step_idx in range(1, tabs_count + 1):
                    print(f"\\n--- Processing Tab {step_idx} ---")
                    # Click the tab to make sure we are on it
                    try:
                        tab_locator = page.locator('.lesson-tab').nth(step_idx - 1)
                        await tab_locator.click(force=True, timeout=5000)
                    except Exception:
                        print("Failed to click tab normally, attempting JS click.")
                        await page.evaluate(f'''() => {{
                            const tabs = document.querySelectorAll('.lesson-tab');
                            if(tabs.length >= {step_idx}) tabs[{step_idx - 1}].click();
                        }}''')
                    
                    await page.wait_for_timeout(1000)
                    
                    # 3. Simulate watching the video
                    print("Fast-forwarding video (simulating slider drag)...")
                    try:
                        # Click the thumbnail to start playing the video so the quiz polling interval starts
                        thumb = page.locator('.custom-thumbnail').nth(step_idx - 1)
                        if await thumb.is_visible():
                            await thumb.click(force=True)
                            await page.wait_for_timeout(1000)
                            
                        # Simulate dragging the slider to 99%
                        await page.evaluate('''() => {
                            const sliders = document.querySelectorAll('.video-seek');
                            sliders.forEach(s => {
                                s.value = 99;
                                s.dispatchEvent(new Event('input', { bubbles: true }));
                                s.dispatchEvent(new Event('change', { bubbles: true }));
                            });
                        }''')
                        await page.wait_for_timeout(3000)
                    except Exception as e:
                        print("Could not manipulate video slider.", e)
                        
                    # Handle the dashboard notice if it blocks the screen
                    try:
                        notice_close_btn = page.locator('.dashboard-notice-close, .dashboard-notice button')
                        if await notice_close_btn.count() > 0 and await notice_close_btn.first.is_visible():
                            print("Notice appeared, closing it...")
                            await notice_close_btn.first.click(force=True)
                            await page.wait_for_timeout(1000)
                    except Exception:
                        pass
                    
                    # Check if a quiz popped up
                    quiz_visible = await page.locator('.quiz-overlay').is_visible()
                    if quiz_visible:
                        print("Quiz detected!")
                        # We will loop to answer all questions in this quiz
                        while await page.locator('.quiz-overlay').is_visible():
                            question_text = await page.locator('.quiz-overlay h3').inner_text() if await page.locator('.quiz-overlay h3').is_visible() else "Question"
                            print(f"Answering question: {question_text}")
                            
                            # Determine type of question
                            await page.wait_for_timeout(500) # Wait for Vue transition
                            has_custom_html = await page.locator('.answer-opt-btn, #mb1-check-btn, #mb2-check-btn, #paren-check-btn, #and-check-btn, #or-check-btn, #logical-check-btn, #needs-check-btn, #wants-check-btn, .ide-run-btn').count() > 0
                            has_choices = await page.locator('.choice-btn, .answer-button').count() > 0
                            has_input = await page.locator('.quiz-input-field, .input-container input').count() > 0
                            has_essay = await page.locator('.quiz-essay-field').is_visible()
                            
                            if has_custom_html:
                                # For custom HTML quizzes, use DOM interactions
                                correct_choice = page.locator('.answer-opt-btn[data-correct="true"]')
                                if await correct_choice.count() > 0:
                                    await correct_choice.first.click()
                                    await page.wait_for_timeout(1000)
                                else:
                                    # Handle custom input quizzes
                                    if await page.locator('#mb1-kw').is_visible():
                                        await page.fill('#mb1-kw', 'elif')
                                        await page.fill('#mb1-cond', 'age<18')
                                        await page.locator('#mb1-check-btn').click()
                                    elif await page.locator('#mb2-val1').is_visible():
                                        await page.fill('#mb2-val1', '90')
                                        await page.fill('#mb2-val2', '80')
                                        await page.locator('#mb2-check-btn').click()
                                    elif await page.locator('#paren-input').is_visible():
                                        await page.fill('#paren-input', 'password_ok and (is_admin or is_premium)')
                                        await page.locator('#paren-check-btn').click()
                                    elif await page.locator('#and-input').is_visible():
                                        await page.fill('#and-input', 'and aktif_organisasi == true')
                                        await page.locator('#and-check-btn').click()
                                    elif await page.locator('#or-input').is_visible():
                                        await page.fill('#or-input', 'or ada_kupon == true')
                                        await page.locator('#or-check-btn').click()
                                    elif await page.locator('#logical-input').is_visible():
                                        await page.fill('#logical-input', 'and (cuaca == "cerah")')
                                        await page.locator('#logical-check-btn').click()
                                    elif await page.locator('.needs-wants-input').is_visible():
                                        inputs = page.locator('.needs-wants-input')
                                        count = await inputs.count()
                                        for i in range(count):
                                            await inputs.nth(i).fill('Testing')
                                        # Click the check button for needs wants
                                        await page.locator('button[onclick*="checkNeedsWantsGuess"]').click()
                                    elif await page.locator('.ide-run-btn').is_visible():
                                        await page.locator('.ide-submit-btn').click()
                                        
                                    await page.wait_for_timeout(1000)
                                    
                            elif has_choices:
                                choices = page.locator('.choice-btn, .answer-button')
                                count = await choices.count()
                                print(f"Found {count} choices. Trying them...")
                                for attempt in range(count):
                                    if await choices.nth(attempt).is_visible():
                                        await choices.nth(attempt).click(force=True)
                                        # Wait 2500ms because Vue UI disables buttons for 2s after a wrong answer
                                        await page.wait_for_timeout(2500)
                                        if await page.locator('.quiz-next, .quiz-next-btn').is_visible():
                                            break
                                
                            elif has_input:
                                print("Input quiz detected. Entering placeholder text...")
                                inputs = page.locator('.quiz-input-field, .input-container input')
                                count = await inputs.count()
                                for i in range(count):
                                    if await inputs.nth(i).is_visible():
                                        await inputs.nth(i).fill("Testing input")
                                        await page.keyboard.press("Enter")
                                await page.wait_for_timeout(1000)
                                
                            elif has_essay:
                                print("Essay quiz detected. Entering placeholder text...")
                                await page.fill('.quiz-essay-field', "Ini adalah jawaban essay testing")
                                await page.click('.essay-submit-btn')
                                await page.wait_for_timeout(1000)
                                
                            # If next button is visible, click it
                            next_btn = page.locator('.quiz-next, .quiz-next-btn').first
                            if await next_btn.is_visible():
                                btn_text = await next_btn.inner_text()
                                print(f"Clicking quiz next button: {btn_text}")
                                await next_btn.click(force=True)
                                await page.wait_for_timeout(1000)
                            else:
                                print("Next button not visible after answering. Real bug found or stuck in quiz!")
                                break
                    else:
                        print("No quiz popped up or video already finished.")

                    # Try to go to next tab via the "Lanjut modul berikutnya" button in the tab body if it exists
                    try:
                        next_step_btn = page.locator('button.next-step-btn')
                        if await next_step_btn.is_visible():
                            await next_step_btn.click()
                            print("Clicked 'Lanjut modul berikutnya' button.")
                    except Exception:
                        pass
                
                print(f"[{url}] Completed processing all tabs.")
                
            except Exception as e:
                print(f"[{url}] Encountered an error: {e}")
            finally:
                await page.close()
                
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
