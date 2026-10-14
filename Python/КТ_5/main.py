from datetime import date
from pathlib import Path
import tkinter as tk


TASK_FILE = Path(__file__).with_name("tasks.txt")


def load_tasks(filename):
    tasks = []
    lines = Path(filename).read_text(encoding="utf-8-sig").splitlines()

    for line_number, line in enumerate(lines, 1):
        if not line.strip():
            continue

        deadline, separator, title = line.partition("|")
        if not separator or not title.strip():
            raise ValueError(f"Строка {line_number}: нужна дата и название через знак |")

        try:
            day = date.fromisoformat(deadline.strip())
        except ValueError:
            raise ValueError(f"Строка {line_number}: проверьте дату {deadline.strip()}") from None

        tasks.append((day, title.strip()))

    return sorted(tasks, key=lambda task: task[0])


def day_word(number):
    number = abs(number) % 100
    if 11 <= number <= 14:
        return "дней"
    if number % 10 == 1:
        return "день"
    if 2 <= number % 10 <= 4:
        return "дня"
    return "дней"


def format_task(deadline, title, today):
    days = (deadline - today).days
    if days < 0:
        return f"{abs(days)} {day_word(days)} назад · {title}", "past"
    if days == 0:
        return f"Сегодня · {title}", "today"
    return f"Через {days} {day_word(days)} · {title}", "future"


class ReminderApp:
    def __init__(self, window, task_file=TASK_FILE):
        self.window = window
        self.task_file = Path(task_file)
        window.title("Дамир · напоминания")
        window.geometry("760x480")
        window.minsize(540, 320)
        window.configure(bg="#111827")

        tk.Label(window, text="Планы Дамира", font=("Segoe UI", 22, "bold"),
                 bg="#111827", fg="#f9fafb").pack(padx=24, pady=(22, 4), anchor="w")

        self.date_label = tk.Label(window, font=("Segoe UI", 11),
                                   bg="#111827", fg="#9ca3af")
        self.date_label.pack(padx=24, anchor="w")

        tk.Label(window, text="Красный — прошло · жёлтый — сегодня · зелёный — впереди",
                 font=("Segoe UI", 10), bg="#111827", fg="#cbd5e1").pack(
                     padx=24, pady=(8, 12), anchor="w")

        content = tk.Frame(window, bg="#111827")
        content.pack(fill="both", expand=True, padx=24)

        scrollbar = tk.Scrollbar(content)
        scrollbar.pack(side="right", fill="y")

        self.items = tk.Text(content, wrap="word", font=("Segoe UI", 12),
                             bg="#111827", fg="#e5e7eb", relief="flat",
                             padx=8, pady=8, spacing3=10, cursor="arrow",
                             yscrollcommand=scrollbar.set)
        self.items.pack(side="left", fill="both", expand=True)
        scrollbar.configure(command=self.items.yview)

        self.items.tag_configure("past", foreground="#f87171")
        self.items.tag_configure("today", foreground="#fbbf24")
        self.items.tag_configure("future", foreground="#86efac")

        tk.Button(window, text="Перечитать файл", command=self.reload_tasks,
                  font=("Segoe UI", 10), padx=14, pady=5).pack(
                      padx=24, pady=16, anchor="e")

        self.reload_tasks()

    def reload_tasks(self):
        today = date.today()
        self.date_label.configure(text=f"Сегодня {today:%d.%m.%Y}")
        self.items.configure(state="normal")
        self.items.delete("1.0", "end")

        try:
            tasks = load_tasks(self.task_file)
        except (OSError, ValueError) as error:
            self.items.insert("end", f"Не удалось прочитать задачи:\n{error}", "past")
        else:
            if not tasks:
                self.items.insert("end", "Пока задач нет. Добавьте их в tasks.txt.")
            for deadline, title in tasks:
                text, color = format_task(deadline, title, today)
                self.items.insert("end", text + "\n", color)

        self.items.configure(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()
