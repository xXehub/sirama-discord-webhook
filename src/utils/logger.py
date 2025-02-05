from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from datetime import datetime

console = Console()

def create_course_table(title, courses_data):
    table = Table(title=title, show_header=True, header_style="bold magenta")
    table.add_column("Tingkat", style="cyan", justify="center")
    table.add_column("Matkul Terload", style="green", justify="center")
    
    total_courses = 0
    for page, count in courses_data:
        table.add_row(str(page), str(count))
        total_courses += count
    
    return table, total_courses

def log_course_data(available_courses_by_page, selected_courses_count, displayed=[False]):
    if not displayed[0]:
        console.print("\n[DATA] 📊 Matkul Data Summary", style="bold blue")
        
        available_table, total_available = create_course_table(
            "Matkul Tersedia dari tingkat",
            [(i+1, len(courses)) for i, courses in enumerate(available_courses_by_page)]
        )
        console.print(available_table)
        
        summary = Panel(
            f"[cyan]Total Matkul Tersedia:[/cyan] {total_available}\n"
            f"[cyan]Total Matkul Dipilih:[/cyan] {selected_courses_count}",
            title="Summary",
            border_style="green"
        )
        console.print(summary)
        
        displayed[0] = True

def log_status(message, style="bold blue", displayed=[False]):
    if not displayed[0]:
        current_time = datetime.now().strftime('%H:%M:%S')
        console.print(f"[{current_time}] {message}", style=style)
        displayed[0] = True

def log_error(message, displayed=[False]):
    if not displayed[0]:
        current_time = datetime.now().strftime('%H:%M:%S')
        console.print(f"[{current_time}] ❌ {message}", style="bold red")
        displayed[0] = True

def log_success(message, displayed=[False]):
    current_time = datetime.now().strftime('%H:%M:%S')
    console.print(f"[{current_time}] ✅ {message}", style="bold green")
        
def print_banner(banner_text):
    console.print(banner_text, style="bold blue")

def log_waiting(seconds):
    console.print(f"\n⏳ Menunggu {seconds} detik sebelum cek ulang...", style="yellow")