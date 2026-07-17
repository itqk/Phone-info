# 📱 Phone-Info

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Termux-red.svg?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-2.0-brightgreen.svg?style=for-the-badge)

![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=00FF00&center=true&vCenter=true&width=435&lines=Advanced+Phone+Information+Tool;Made+with+%E2%9D%A4+by+%40FushiCode;Stay+Safe+%26+Secure)

## 📌 Overview

**Phone-Info** is a CLI-based phone number information tool that provides validation and carrier details for Indian phone numbers. It combines a lightweight online lookup with offline validation via the `phonenumbers` library, presented in a clean, colorful terminal interface.

### ✨ Features

- 🔍 **Dual Data Source** — combines online lookup and the offline `phonenumbers` library
- 📊 **Carrier & Format Info** — carrier, line type, timezone, and number formatting
- 🎨 **Beautiful CLI Interface** — rich colors, animations, and clean formatting
- ⚡ **Fast & Lightweight** — quick responses, minimal resource usage
- 🌐 **Cross-Platform** — works on Linux, macOS, and Termux
- 🎯 **Indian Number Support** — optimized for Indian phone numbers

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)
- Git (optional, for cloning)

### Method 1: Using Git (Recommended)

```bash
# Clone the repository
git clone https://github.com/itqk/Phone-info.git

# Navigate to the directory
cd Phone-info

# Install dependencies
pip install -r requirements.txt

# Run the tool
python Phone-info.py
```

### Method 2: Direct Download

```bash
# Download the script
wget https://raw.githubusercontent.com/itqk/Phone-info/main/Phone-info.py

# Install dependencies
pip install requests phonenumbers pyfiglet rich colorama

# Run the tool
python Phone-info.py
```

### Method 3: Termux Installation

```bash
# Update packages
pkg update && pkg upgrade

# Install Python
pkg install python

# Clone repository
git clone https://github.com/itqk/Phone-info.git

# Navigate to directory
cd Phone-info

# Install dependencies
pip install -r requirements.txt

# Run the tool
python Phone-info.py
```

## 📦 Dependencies

All dependencies are listed in `requirements.txt`:

```text
requests
phonenumbers
pyfiglet
rich
colorama
```

Install all at once:

```bash
pip install -r requirements.txt
```

## 🎮 Usage

### Basic Usage

1. Run the script:
   ```bash
   python Phone-info.py
   ```
2. **Enter a phone number**
   - Format: 10 digits (e.g., `9876543210`)
   - Or with country code: `+91XXXXXXXXXX`
3. **View results**
   - Online lookup data
   - Offline data (from the `phonenumbers` library)
   - Validation results and number formats
4. **Continue or exit**
   - Type `y` to search another number
   - Type `n` or press `q` to exit

### Quick Commands

| Command | Description |
|---|---|
| `python Phone-info.py` | Run the tool |
| `q` | Exit the tool |
| *10-digit number* | Search for information |

### Example

```bash
$ python Phone-info.py

📱 Enter phone number details:
   Format: 10 digits or +91XXXXXXXXXX
   Press 'q' to exit

└──> Number: 9876543210

# Output will display:
# - Online lookup data
# - Offline data (phonenumbers library)
# - Validation results
# - Number formats
```

## 📊 Output Information

### 🌐 Online Data

- Country and state
- SIM card provider
- Connection type (Prepaid/Postpaid)
- Reference/hometown city

### 📡 Offline Data (`phonenumbers` library)

- Country name and region code
- Carrier information
- Timezone
- Number type (Fixed line / Mobile / VoIP / etc.)
- Validation status
- Number formats (E.164, International, National, RFC3966)

> **Note:** This tool only reports information that is derivable from the number itself (validity, carrier, region, line type) or available through public lookup services. It does not access or expose personal subscriber data such as an owner's name, address, device identifiers, or location history — that kind of data isn't available through any legitimate public API.

## 📁 Project Structure

```text
Phone-info/
├── Phone-info.py          # Main script
├── requirements.txt       # Dependencies
├── README.md              # Documentation
└── LICENSE                # License file
```

## 👨‍💻 Developer

![Developer Avatar](https://avatars.githubusercontent.com/itqk)

**@FushiCode**
Full Stack Developer & Security Enthusiast

### Connect with Developer

[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/fushicode)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/fushicode)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/itqk)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational and informational purposes only.

- Do not use this tool for illegal activities
- Respect privacy and data protection laws
- The developer is not responsible for any misuse
- Use responsibly and ethically

## 🙏 Acknowledgments

- [phonenumbers](https://github.com/daviddrysdale/python-phonenumbers) library
- [Rich](https://github.com/Textualize/rich) for beautiful CLI
- [Colorama](https://github.com/tartley/colorama) for cross-platform colors
- [pyfiglet](https://github.com/pwaller/pyfiglet) for ASCII banners

## ⭐ Support

If you find this tool useful, please consider:

- ⭐ Starring the repository
- 🔄 Sharing it with others
- 🐛 Reporting issues
- 💡 Suggesting new features

Made with ❤️ by [@FushiCode](https://github.com/itqk)

**⭐ Star this repo if you like it! ⭐**

## 📞 Contact

For support, queries, or collaboration:

- 💬 Telegram: [@FushiCode](https://t.me/fushicode)
- 📷 Instagram: [@fushicode](https://instagram.com/fushicode)

![Footer SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=18&pause=1000&color=00FF00&center=true&vCenter=true&width=435&lines=Happy+Coding!+;Stay+Safe!;Keep+Learning!)
