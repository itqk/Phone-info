#!/usr/bin/env python3
"""
Phone Info Tool - Enhanced CLI Edition
Developer: @FushiCode
"""

import requests
import json
import os
import sys
import time
from datetime import datetime
from typing import Dict, Any, Optional

# Import rich for beautiful CLI
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.columns import Columns
from rich.text import Text
from rich import box
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.align import Align
from rich.style import Style
from rich.prompt import Prompt, Confirm

# Import colorama for colors
from colorama import init, Fore, Back, Style as ColoramaStyle
init(autoreset=True)

# Import phonenumbers
try:
    import phonenumbers
    from phonenumbers import (
        geocoder,
        carrier,
        timezone,
        PhoneNumberFormat,
        PhoneNumberType
    )
except ImportError:
    os.system("pip install phonenumbers")
    import phonenumbers
    from phonenumbers import (
        geocoder,
        carrier,
        timezone,
        PhoneNumberFormat,
        PhoneNumberType
    )

try:
    import pyfiglet
except ImportError:
    os.system("pip install pyfiglet")
    import pyfiglet

# Initialize Rich console
console = Console()

# ============= UTILITY FUNCTIONS =============
def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def loading_animation(message: str = "Processing", duration: float = 2):
    """Display loading animation using Rich"""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task(f"[cyan]{message}...", total=None)
        time.sleep(duration)

def get_banner() -> str:
    """Generate ASCII banner"""
    banner = pyfiglet.figlet_format("Phone Info", font="slant")
    return banner

def create_header():
    """Create beautiful header with rich"""
    clear_screen()
    
    # Banner with gradient effect
    banner_text = get_banner()
    console.print(banner_text, style="bold red")
    
    # Create header panel
    header_content = f"""
[bold yellow]📱 ADVANCED PHONE INFORMATION TOOL[/bold yellow]
[cyan]👨‍💻 Developer: @FushiCode[/cyan]
[green]📌 Version: 2.0 | 🐍 Python 3.x[/green]
[dim]🔒 Privacy Focused | 📊 Real-time Data[/dim]
    """
    
    panel = Panel(
        Align.center(header_content),
        border_style="cyan",
        box=box.HEAVY,
        width=80
    )
    console.print(panel)
    console.print()

def create_result_panel(phone: str, api_data: Optional[Dict], offline_data: Dict):
    """Create beautiful result display using Rich panels and tables"""
    
    # Main panel with phone number
    phone_display = f"[bold yellow]📞 Phone Number:[/bold yellow] [bold white]{phone}[/bold white]"
    main_panel = Panel(
        Align.center(phone_display),
        border_style="green",
        box=box.DOUBLE,
        width=80
    )
    console.print(main_panel)
    console.print()
    
    # Online Data Table
    if api_data:
        console.print("[bold cyan]🌐 ONLINE DATA[/bold cyan]", style="bold cyan")
        console.print("─" * 80)
        
        online_table = Table(show_header=False, box=box.MINIMAL, padding=(0, 2))
        online_table.add_column("Key", style="cyan", width=25)
        online_table.add_column("Value", style="white", width=50)
        
        for key, value in api_data.items():
            # Special formatting for certain fields
            if key == 'Owner Personality':
                value = f"[magenta italic]{value}[/magenta italic]"
            elif key == 'Owner Name':
                if len(str(value)) > 3:
                    value = f"[red bold blink]🔒 PRIVATE 🔒[/red bold blink]"
            elif key == 'Complaints':
                value = f"[yellow]{value}[/yellow]"
            elif key == 'Connection':
                value = f"[green]{value}[/green]"
            elif key == 'SIM card':
                value = f"[blue]{value}[/blue]"
            elif key == 'Mobile State':
                value = f"[magenta]{value}[/magenta]"
            elif key == 'Country':
                value = f"[cyan]{value}[/cyan]"
            
            # Truncate long values
            if isinstance(value, str) and len(value) > 40:
                value = value[:37] + "..."
            
            online_table.add_row(key, str(value))
        
        console.print(online_table)
        console.print()
    
    # Offline Data Table
    console.print("[bold magenta]📡 OFFLINE DATA[/bold magenta]", style="bold magenta")
    console.print("─" * 80)
    
    offline_table = Table(show_header=False, box=box.MINIMAL, padding=(0, 2))
    offline_table.add_column("Category", style="cyan", width=25)
    offline_table.add_column("Value", style="white", width=50)
    
    if 'error' not in offline_data:
        # Validation
        valid_status = "✅ Yes" if offline_data.get('is_valid') else "❌ No"
        possible_status = "✅ Yes" if offline_data.get('is_possible') else "❌ No"
        
        offline_items = [
            ("🌍 Country", offline_data.get('country', 'Unknown')),
            ("📍 Region", offline_data.get('region_code', 'Unknown')),
            ("📱 Carrier", offline_data.get('carrier', 'Unknown')),
            ("🕐 Timezone", offline_data.get('timezone', 'Unknown')),
            ("📊 Number Type", offline_data.get('number_type', 'Unknown')),
            ("✅ Valid Number", valid_status),
            ("🔢 Possible Number", possible_status),
        ]
        
        for category, value in offline_items:
            # Color coding for values
            if isinstance(value, str) and value.startswith('✅'):
                value = f"[green]{value}[/green]"
            elif isinstance(value, str) and value.startswith('❌'):
                value = f"[red]{value}[/red]"
            elif category == "📱 Carrier" and value != 'Unknown':
                value = f"[blue]{value}[/blue]"
            elif category == "🌍 Country":
                value = f"[cyan]{value}[/cyan]"
            
            offline_table.add_row(category, str(value))
        
        # Formats section
        offline_table.add_row("[bold]📋 Formats[/bold]", "", style="bold yellow")
        formats = [
            ('E164', offline_data.get('e164', 'N/A')),
            ('International', offline_data.get('international', 'N/A')),
            ('National', offline_data.get('national', 'N/A')),
            ('RFC3966', offline_data.get('rfc3966', 'N/A')),
        ]
        
        for fmt_label, fmt_value in formats:
            offline_table.add_row(f"  {fmt_label}", fmt_value)
    
    console.print(offline_table)
    console.print()
    
    # Footer with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    footer = Panel(
        f"[dim]📅 {timestamp} | 👨‍💻 @FushiCode[/dim]",
        border_style="dim",
        box=box.HORIZONTALS,
        width=80
    )
    console.print(footer)

def fetch_phone_info(phone: str) -> Optional[Dict[str, Any]]:
    """Fetch phone information from API"""
    url = f'https://api-calltracer-eternal.vercel.app/api?number={phone}'
    
    console.print("[cyan]🔍 Connecting to server...[/cyan]")
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def get_phonenumbers_info(phone: str) -> Dict[str, Any]:
    """Get offline phone number details"""
    details = {}
    try:
        num = phonenumbers.parse(phone)
        
        # Basic info
        details['raw'] = str(num)
        details['country_code'] = num.country_code
        details['national_number'] = num.national_number
        details['extension'] = num.extension
        
        # Validation
        details['is_valid'] = phonenumbers.is_valid_number(num)
        details['is_possible'] = phonenumbers.is_possible_number(num)
        
        # Region
        details['region_code'] = phonenumbers.region_code_for_number(num)
        details['country'] = geocoder.description_for_number(num, "en")
        
        # Carrier
        details['carrier'] = carrier.name_for_number(num, "en")
        
        # Timezone
        timezones = timezone.time_zones_for_number(num)
        details['timezone'] = ", ".join(timezones) if timezones else "Unknown"
        
        # Formats
        details['e164'] = phonenumbers.format_number(num, PhoneNumberFormat.E164)
        details['international'] = phonenumbers.format_number(num, PhoneNumberFormat.INTERNATIONAL)
        details['national'] = phonenumbers.format_number(num, PhoneNumberFormat.NATIONAL)
        details['rfc3966'] = phonenumbers.format_number(num, PhoneNumberFormat.RFC3966)
        
        # Type
        num_type = phonenumbers.number_type(num)
        type_map = {
            PhoneNumberType.FIXED_LINE: "Fixed Line",
            PhoneNumberType.MOBILE: "Mobile",
            PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed/Mobile",
            PhoneNumberType.TOLL_FREE: "Toll Free",
            PhoneNumberType.PREMIUM_RATE: "Premium Rate",
            PhoneNumberType.SHARED_COST: "Shared Cost",
            PhoneNumberType.VOIP: "VoIP",
            PhoneNumberType.PERSONAL_NUMBER: "Personal",
            PhoneNumberType.PAGER: "Pager",
            PhoneNumberType.UAN: "UAN",
            PhoneNumberType.VOICEMAIL: "Voicemail",
            PhoneNumberType.UNKNOWN: "Unknown",
        }
        details['number_type'] = type_map.get(num_type, "Unknown")
        
    except phonenumbers.NumberParseException as e:
        details['error'] = str(e)
    
    return details

def display_phone_info(phone: str, api_data: Optional[Dict[str, Any]], offline_data: Dict[str, Any]):
    """Display all phone information with rich formatting"""
    create_result_panel(phone, api_data, offline_data)

def validate_phone_number(phone: str) -> tuple:
    """Validate and clean phone number"""
    # Remove +91 if present
    if phone.startswith("+91"):
        clean_phone = phone[3:]
    else:
        clean_phone = phone
    
    # Validate
    if clean_phone.isdigit() and len(clean_phone) == 10:
        return True, clean_phone, "+91" + clean_phone
    else:
        return False, None, None

def process_phone_number(phone: str):
    """Process and display phone information"""
    # Validate
    is_valid, clean_phone, full_phone = validate_phone_number(phone)
    
    if not is_valid:
        console.print("[red]❌ Invalid phone number! Please enter a valid Indian number (10 digits).[/red]")
        return
    
    # Show processing
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        
        task = progress.add_task("[cyan]Fetching online data...", total=100)
        api_data = fetch_phone_info(clean_phone)
        progress.update(task, advance=50)
        
        task2 = progress.add_task("[magenta]Fetching offline data...", total=100)
        offline_data = get_phonenumbers_info(full_phone)
        progress.update(task2, advance=50)
        
        time.sleep(0.5)
    
    # Clear screen and display results
    clear_screen()
    create_header()
    display_phone_info(full_phone, api_data, offline_data)

# ============= MAIN FUNCTION =============
def main():
    """Main program loop"""
    try:
        while True:
            create_header()
            
            # Input section with rich prompt
            console.print()
            console.print("[yellow]📱 Enter phone number details:[/yellow]")
            console.print("[dim]   Format: 10 digits or +91XXXXXXXXXX[/dim]")
            console.print("[dim]   Press 'q' to exit[/dim]")
            console.print()
            
            phone = Prompt.ask("[cyan]└──>[/cyan] [yellow]Number[/yellow]")
            
            if phone.lower() == 'q':
                console.print()
                console.print("[bold green]👋 Thanks for using Phone Info Tool! Goodbye![/bold green]")
                sys.exit(0)
            
            # Process the phone number
            process_phone_number(phone)
            
            # Continue prompt
            console.print()
            if not Confirm.ask("[cyan]Do you want to search another number?[/cyan]", default=True):
                console.print("[bold green]👋 Thanks for using Phone Info Tool! Goodbye![/bold green]")
                break
            
            # Clear screen for next search
            clear_screen()
    
    except KeyboardInterrupt:
        console.print()
        console.print("[yellow]👋 Interrupted by user. Goodbye![/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]❌ An error occurred: {e}[/red]")
        sys.exit(1)

if __name__ == "__main__":
    main()