import calendar
from datetime import datetime

def generate_calendar_html(month, year, week_start='sunday', title_text=None, 
                          primary_color='#2c3e50', accent_color='#e74c3c',
                          bg_color='#ecf0f1', font_family='Georgia'):
    """
    Generate a printable HTML calendar.
    
    Args:
        month: 1-12
        year: e.g., 2024
        week_start: 'sunday' or 'monday'
        title_text: Custom title (default: "Month Year")
        primary_color: Main text color
        accent_color: Header/accent color
        bg_color: Background color
        font_family: Font choice
    """
    
    # Set calendar start day
    if week_start.lower() == 'monday':
        calendar.setfirstweekday(calendar.MONDAY)
        day_headers = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    else:
        calendar.setfirstweekday(calendar.SUNDAY)
        day_headers = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    
    # Get calendar data
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    
    # Custom title or default
    if title_text is None:
        title_text = f"{month_name} {year}"
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title_text}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        @media print {{
            body {{
                margin: 0;
            }}
            .no-print {{
                display: none;
            }}
        }}
        
        body {{
            font-family: {font_family}, serif;
            background: {bg_color};
            padding: 2rem;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }}
        
        .calendar-container {{
            background: white;
            padding: 3rem;
            border-radius: 2px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.1);
            max-width: 900px;
            width: 100%;
        }}
        
        .calendar-header {{
            text-align: center;
            margin-bottom: 2.5rem;
            position: relative;
            padding-bottom: 1.5rem;
        }}
        
        .calendar-header::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 3px;
            background: {accent_color};
        }}
        
        .calendar-title {{
            font-size: 2.8rem;
            font-weight: 300;
            letter-spacing: 0.05em;
            color: {primary_color};
            text-transform: uppercase;
        }}
        
        .calendar-grid {{
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 1px;
            background: #e0e0e0;
            border: 1px solid #e0e0e0;
        }}
        
        .day-header {{
            background: {accent_color};
            color: white;
            padding: 1rem;
            text-align: center;
            font-weight: 600;
            font-size: 0.85rem;
            letter-spacing: 0.1em;
            text-transform: uppercase;
        }}
        
        .day-cell {{
            background: white;
            min-height: 100px;
            padding: 0.8rem;
            position: relative;
        }}
        
        .day-cell.empty {{
            background: #f9f9f9;
        }}
        
        .day-number {{
            font-size: 1.5rem;
            font-weight: 300;
            color: {primary_color};
            line-height: 1;
        }}
        
        .day-cell.weekend .day-number {{
            color: {accent_color};
        }}
        
        .print-button {{
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            padding: 1rem 2rem;
            background: {accent_color};
            color: white;
            border: none;
            border-radius: 4px;
            font-family: {font_family}, serif;
            font-size: 1rem;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            transition: all 0.3s ease;
        }}
        
        .print-button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(0,0,0,0.2);
        }}
    </style>
</head>
<body>
    <div class="calendar-container">
        <div class="calendar-header">
            <h1 class="calendar-title">{title_text}</h1>
        </div>
        
        <div class="calendar-grid">
"""
    
    # Day headers
    for day in day_headers:
        html += f'            <div class="day-header">{day}</div>\n'
    
    # Calendar days
    for week in cal:
        for i, day in enumerate(week):
            if day == 0:
                html += '            <div class="day-cell empty"></div>\n'
            else:
                # Check if weekend (indices 0 and 6 for Sunday start, 5 and 6 for Monday start)
                is_weekend = (week_start.lower() == 'sunday' and i in [0, 6]) or \
                           (week_start.lower() == 'monday' and i in [5, 6])
                weekend_class = ' weekend' if is_weekend else ''
                html += f'            <div class="day-cell{weekend_class}"><span class="day-number">{day}</span></div>\n'
    
    html += """        </div>
    </div>
    
    <button class="print-button no-print" onclick="window.print()">Print Calendar</button>
</body>
</html>"""
    
    return html


def save_calendar(month, year, filename=None, **kwargs):
    """Save calendar to HTML file."""
    if filename is None:
        filename = f"calendar_{year}_{month:02d}.html"
    
    html = generate_calendar_html(month, year, **kwargs)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return filename


if __name__ == "__main__":
    print("=== Calendar Maker ===\n")
    
    # Get user input
    while True:
        try:
            month = int(input("Enter month (1-12): "))
            if 1 <= month <= 12:
                break
            print("Month must be between 1 and 12")
        except ValueError:
            print("Please enter a valid number")
    
    while True:
        try:
            year = int(input("Enter year (e.g., 2024): "))
            if year > 0:
                break
            print("Year must be positive")
        except ValueError:
            print("Please enter a valid number")
    
    # Customization options
    print("\n--- Customization (press Enter for defaults) ---")
    
    week_start = input("Week starts on (sunday/monday) [sunday]: ").strip().lower() or 'sunday'
    title = input("Custom title (leave empty for default): ").strip() or None
    primary = input("Primary color hex (e.g., #2c3e50) [default]: ").strip() or '#2c3e50'
    accent = input("Accent color hex (e.g., #e74c3c) [default]: ").strip() or '#e74c3c'
    bg = input("Background color hex (e.g., #ecf0f1) [default]: ").strip() or '#ecf0f1'
    font = input("Font family (e.g., Georgia, Arial, Courier) [Georgia]: ").strip() or 'Georgia'
    
    # Generate calendar
    filename = save_calendar(
        month, year,
        week_start=week_start,
        title_text=title,
        primary_color=primary,
        accent_color=accent,
        bg_color=bg,
        font_family=font
    )
    
    print(f"\n✓ Calendar saved to: {filename}")
    print("Open in browser and use the Print button to save as PDF")
