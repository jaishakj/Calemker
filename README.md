# Calemker

A minimal Python calendar generator that creates beautiful, printable HTML calendars with full customization support.

## Features

- **Clean HTML Output** - Generates print-ready calendars that open in any browser
- **Full Customization** - Control colors, fonts, titles, and week start day
- **Responsive Design** - Looks good on screen and perfect for printing
- **Zero Dependencies** - Uses only Python's standard library
- **PDF Export** - Print directly to PDF from your browser

## Installation

No installation required. Just Python 3.6+.

```bash
git clone <your-repo-url>
cd calemker
```

## Usage

### Basic Usage

```bash
python calemker.py
```

Follow the prompts:
1. Enter month (1-12)
2. Enter year (e.g., 2024)
3. Customize or press Enter for defaults

### Programmatic Usage

```python
from calemker import save_calendar

# Default calendar
save_calendar(month=3, year=2024)

# Custom calendar
save_calendar(
    month=12,
    year=2024,
    week_start='monday',
    title_text='Holiday Schedule',
    primary_color='#1a1a2e',
    accent_color='#ff6b6b',
    bg_color='#f0f0f0',
    font_family='Helvetica'
)
```

### Function Reference

```python
generate_calendar_html(month, year, **options)
```

**Parameters:**
- `month` (int): 1-12
- `year` (int): Any valid year
- `week_start` (str): 'sunday' or 'monday' (default: 'sunday')
- `title_text` (str): Custom title (default: "Month Year")
- `primary_color` (str): Main text color hex (default: '#2c3e50')
- `accent_color` (str): Header/weekend color hex (default: '#e74c3c')
- `bg_color` (str): Background color hex (default: '#ecf0f1')
- `font_family` (str): Font name (default: 'Georgia')

**Returns:** HTML string

```python
save_calendar(month, year, filename=None, **options)
```

**Parameters:**
- Same as `generate_calendar_html()`
- `filename` (str): Output filename (default: 'calendar_YYYY_MM.html')

**Returns:** Filename string

## Customization Examples

### Dark Theme
```python
save_calendar(
    month=6,
    year=2024,
    primary_color='#e0e0e0',
    accent_color='#00d4ff',
    bg_color='#1a1a1a',
    font_family='Courier'
)
```

### Pastel Theme
```python
save_calendar(
    month=4,
    year=2024,
    primary_color='#5f5f5f',
    accent_color='#ffa5b4',
    bg_color='#fffef9',
    font_family='Arial'
)
```

### Minimal Black & White
```python
save_calendar(
    month=9,
    year=2024,
    primary_color='#000000',
    accent_color='#333333',
    bg_color='#ffffff',
    font_family='Helvetica'
)
```

## Output

The script generates HTML files like `calendar_2024_03.html`. Open in any browser and click "Print Calendar" to:
- Print directly to paper
- Save as PDF
- Adjust print settings (margins, orientation, etc.)

## Browser Compatibility

Works in all modern browsers:
- Chrome/Edge (recommended for PDF export)
- Firefox
- Safari
- Opera

## Tips

- **Best Print Quality**: Use Chrome/Edge, set margins to "None" or "Minimum"
- **Custom Fonts**: Use web-safe fonts or add `@font-face` rules to the HTML
- **Multiple Months**: Run the script multiple times or modify to loop through months
- **Advanced Styling**: Edit the generated HTML file directly for one-off customizations

## Examples

```bash
# Quick February 2024 calendar with defaults
python calemker.py
# Input: 2, 2024, then press Enter for all defaults

# Custom work calendar
python calemker.py
# Input: 3, 2024, monday, "Q1 Planning", #2c3e50, #3498db, #ecf0f1, Arial

# Minimal aesthetic
python calemker.py
# Input: 12, 2024, sunday, "", #000000, #666666, #ffffff, Courier
```

## License

MIT

## Contributing

Pull requests welcome. Keep it minimal and focused.

## Author

Built with Python's `calendar` module - https://docs.python.org/3/library/calendar.html
