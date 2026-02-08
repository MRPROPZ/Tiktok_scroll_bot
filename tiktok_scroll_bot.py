from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException, NoSuchWindowException
from webdriver_manager.chrome import ChromeDriverManager
import time
import psutil

def tiktok_auto_scroll():
    driver = None
    chrome_pids = []  # เก็บ PIDs ของ Chrome ที่เราเปิด
    
    try:
        # ตั้งค่า Chrome
        options = webdriver.ChromeOptions()
        
        # เปิดเบราว์เซอร์
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
        # เก็บ PID ของ Chrome processes ที่เปิดใหม่
        try:
            driver_service_pid = driver.service.process.pid
            parent = psutil.Process(driver_service_pid)
            chrome_pids = [child.pid for child in parent.children(recursive=True)]
            chrome_pids.append(driver_service_pid)
            # โค้ดสำหรับเช็ค PIDs 
            #print(f"📌 ติดตาม Chrome PIDs: {chrome_pids}")
        except:
            pass

        # เปิด TikTok
        driver.get('https://www.tiktok.com/foryou')
        
        print("กำลังเปิด TikTok...")
        time.sleep(5)
        
        print("เริ่มเลื่อนคลิปทุก 10 วินาที (กด Ctrl+C เพื่อหยุด)")
        
        while True:
            try:
                body = driver.find_element(By.TAG_NAME, 'body')
                body.send_keys(Keys.ARROW_DOWN)
                print("เลื่อนไปคลิปถัดไป")
                time.sleep(10)
                
            except (NoSuchWindowException, WebDriverException):
                print("\n⚠️ ตรวจพบว่าเบราว์เซอร์ถูกปิด - หยุดการทำงาน")
                break
            
    except KeyboardInterrupt:
        print("\n✋ ผู้ใช้กด Ctrl+C - กำลังปิดเบราว์เซอร์...")
    except Exception as e:
        print(f"\n❌ เกิดข้อผิดพลาด: {e}")
    finally:
        if driver:
            try:
                driver.quit()
                time.sleep(0.5)
            except:
                pass
            
            # ใช้ psutil ปิดเฉพาะ Chrome ที่ bot เปิด
            print("🔄 กำลังปิด Google Chrome")
            killed_count = 0
            
            for pid in chrome_pids:
                try:
                    process = psutil.Process(pid)
                    process_name = process.name()
                    process.kill()
                    print(f"  ✅ ปิด {process_name} (PID: {pid})")
                    killed_count += 1
                except psutil.NoSuchProcess:
                    pass  # Process ปิดไปแล้ว
                except Exception as e:
                    print(f"  ⚠️ ไม่สามารถปิด PID {pid}: {e}")
            
            if killed_count > 0:
                print(f"✅ ปิด Chrome processes สำเร็จ {killed_count} processes")
            else:
                print("ℹ️ Chrome processes ถูกปิดไปแล้ว")

if __name__ == "__main__":
    tiktok_auto_scroll()