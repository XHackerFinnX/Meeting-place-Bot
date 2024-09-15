import datetime
import os

async def log_message(sender: str, user_id: str, message: str):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{formatted_time}: {sender} - {message}"

    log_folder = r"log/message_history"

    # Создаем папку, если она не существует
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    # Создайте файл или откройте существующий для записи
    log_file_path = os.path.join(log_folder, f"user_{user_id}_chat_log.txt")
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry + "\n")
        
        
# https://api.telegram.org/bot7003174677:AAFcpQcAVLJB3myEr_0oWxyOzYlT7qQtsRs/getUpdates