from rich.console import Console
from tqdm import tqdm

console = Console()

def print_start(title: str):
    console.print(f"[bold cyan]🐶 작업 시작: {title}[/bold cyan]")

def print_epoch_summary(epoch_index: int, average_loss: float):
    console.print(f"[bold blue]⚙️ Epoch {epoch_index} Summary[/bold blue]")
    console.print(f"[green]평균 Training Loss:[/green] {average_loss:.4f}")

def print_validation_accuracy(accuracy: float, min_prob: float, max_prob: float):
    console.print(f"[bold green]✅ Val Accuracy:[/bold green] {accuracy:.4f}")
    console.print(f"[dim]Probability range: {min_prob:.3f}–{max_prob:.3f}[/dim]")

def progress_bar(iterable, description: str):
    return tqdm(iterable, desc=description, ncols=80)

def print_success(message: str):
    console.print(f"[bold green]✅ {message}[/bold green]")

def print_warning(message: str):
    console.print(f"[bold yellow]⚠️ {message}[/bold yellow]")

def print_error(message: str):
    console.print(f"[bold red]❌ {message}[/bold red]")

def count_parameters(model):
    total = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    console.print(f"[bold purple]🦄 총 파라미터: {total:,}[/bold purple]")
    console.print(f"[bold purple]🦄 학습 파라미터: {trainable:,}[/bold purple]")
