#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════╗
║                        HAKKO AI                               ║
║        Beautiful Terminal AI for Termux & Kali Linux          ║
║              Powered by OpenRouter GPT-OSS-20B                ║
╚═══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import time
from typing import Optional, Dict, List
from datetime import datetime

try:
    import requests
except ImportError:
    print("Installing requests...")
    os.system("pip install requests")
    import requests

# Beautiful colors optimized for Termux & Kali Linux
class Colors:
    # Main colors
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m' 
    
    # Styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    
    # Bright (perfect for dark terminals)
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_PURPLE = '\033[95m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_BLUE = '\033[94m' # Fix for AttributeError

class HakkoAI:
    """HakkoAI - Premium AI Assistant for Termux & Kali Linux"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize HakkoAI with OpenRouter API
        
        Args:
            api_key: OpenRouter API key
        """
        self.api_key = api_key or os.getenv('OPENROUTER_API_KEY')
        
        # OpenRouter API Configuration
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.model = "openai/gpt-3.5-turbo"  # You can change this
        
        self.conversation_history: List[Dict] = []
        self.current_mode = "chat"
        self.session_start = datetime.now()
        self.message_count = 0
        
        if not self.api_key:
            self.print_error("No API key found!")
            print(f"{Colors.BRIGHT_YELLOW}💡 Set OPENROUTER_API_KEY environment variable{Colors.END}")
            print(f"{Colors.CYAN}   Or edit the script and add your key{Colors.END}\n")
            sys.exit(1)
    
    @staticmethod
    def print_banner():
        """Beautiful banner optimized for Termux & Kali"""
        banner = f"""
{Colors.BRIGHT_CYAN}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║    {Colors.BRIGHT_PURPLE}██╗  ██╗ █████╗ ██╗  ██╗██╗  ██╗ ██████╗      █████╗ ██╗{Colors.BRIGHT_CYAN}      ║
║    {Colors.BRIGHT_PURPLE}██║  ██║██╔══██╗██║ ██╔╝██║ ██╔╝██╔═══██╗    ██╔══██╗██║{Colors.BRIGHT_CYAN}      ║
║    {Colors.BRIGHT_PURPLE}███████║███████║█████╔╝ █████╔╝ ██║   ██║    ███████║██║{Colors.BRIGHT_CYAN}      ║
║    {Colors.BRIGHT_PURPLE}██╔══██║██╔══██║██╔═██╗ ██╔═██╗ ██║   ██║    ██╔══██║██║{Colors.BRIGHT_CYAN}      ║
║    {Colors.BRIGHT_PURPLE}██║  ██║██║  ██║██║  ██╗██║  ██╗╚██████╔╝    ██║  ██║██║{Colors.BRIGHT_CYAN}      ║
║    {Colors.BRIGHT_PURPLE}╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝     ╚═╝  ╚═╝╚═╝{Colors.BRIGHT_CYAN}      ║
║                                                                   ║
║          {Colors.BRIGHT_GREEN}✨ Terminal AI for Termux & Kali Linux ✨{Colors.BRIGHT_CYAN}           ║
║                {Colors.BRIGHT_YELLOW}🚀 Powered by OpenRouter GPT 🚀{Colors.BRIGHT_CYAN}                ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
{Colors.END}
{Colors.BOLD}{Colors.BRIGHT_PURPLE}┌───────────────────────────────────────────────────────────────────┐{Colors.END}
{Colors.BOLD}{Colors.BRIGHT_PURPLE}│{Colors.END}  {Colors.BOLD}{Colors.BRIGHT_CYAN}🎯 COMMANDS{Colors.END}                                                        {Colors.BOLD}{Colors.BRIGHT_PURPLE}│{Colors.END}
{Colors.BOLD}{Colors.BRIGHT_PURPLE}├───────────────────────────────────────────────────────────────────┤{Colors.END}
{Colors.BOLD}{Colors.BRIGHT_PURPLE}│{Colors.END}  {Colors.BRIGHT_GREEN}💬 /chat{Colors.END}      → Friendly conversation mode                       {Colors.BOLD}{Colors.BRIGHT_PURPLE}│{Colors.END}
{Colors.BOLD}{Colors.BRIGHT_PURPLE}│{Colors.END}  {Colors.BRIGHT_CYAN}💻 /code{Colors.END}      → Programming & hacking assistant                  {Colors.BOLD}{Colors.BRIGHT_PURPLE}│{Colors.END}
{Colors.BOLD}{Colors.BRIGHT_PURPLE}│{Colors.END}  {Colors.BRIGHT_YELLOW}🔍 /search{Colors.END}    → Research & information mode                      {Colors.BOLD}{Colors.BRIGHT_PURPLE}│{Colors.END}
{Colors.BOLD}{Colors.BRIGHT_PURPLE}│{Colors.END}  {Colors.BRIGHT_PURPLE}🎨 /creative{Colors.END}  → Creative writing & ideas                         {Colors.BOLD}{Colors.BRIGHT_PURPLE}│{Colors.END}
{Colors.BOLD}{Colors.BRIGHT_PURPLE}│{Colors.END}  {Colors.CYAN}🧹 /clear{Colors.END}     → Clear conversation history                       {Colors.BOLD}{Colors.BRIGHT_PURPLE}│{Colors.END}
{Colors.BOLD}{Colors.BRIGHT_PURPLE}│{Colors.END}  {Colors.YELLOW}📊 /stats{Colors.END}     → Show session statistics                           {Colors.BOLD}{Colors.BRIGHT_PURPLE}│{Colors.END}
{Colors.BOLD}{Colors.BRIGHT_PURPLE}│{Colors.END}  {Colors.BLUE}❓ /help{Colors.END}      → Show this menu                                    {Colors.BOLD}{Colors.BRIGHT_PURPLE}│{Colors.END}
{Colors.BOLD}{Colors.BRIGHT_PURPLE}│{Colors.END}  {Colors.RED}🚪 /exit{Colors.END}      → Exit HakkoAI                                      {Colors.BOLD}{Colors.BRIGHT_PURPLE}│{Colors.END}
{Colors.BOLD}{Colors.BRIGHT_PURPLE}└───────────────────────────────────────────────────────────────────┘{Colors.END}

{Colors.BRIGHT_CYAN}═══════════════════════════════════════════════════════════════════{Colors.END}
"""
        print(banner)
    
    @staticmethod
    def print_error(message: str):
        """Print beautiful error message"""
        print(f"\n{Colors.BRIGHT_RED}{Colors.BOLD}╔═══════════════════════════════════════╗{Colors.END}")
        print(f"{Colors.BRIGHT_RED}{Colors.BOLD}║  ❌ ERROR                            ║{Colors.END}")
        print(f"{Colors.BRIGHT_RED}{Colors.BOLD}╚═══════════════════════════════════════╝{Colors.END}")
        print(f"{Colors.BRIGHT_RED}{message}{Colors.END}\n")
    
    @staticmethod
    def print_success(message: str):
        """Print beautiful success message"""
        print(f"{Colors.BRIGHT_GREEN}{Colors.BOLD}✨ {message} ✨{Colors.END}")
    
    @staticmethod
    def print_thinking():
        """Animated thinking for Termux/Kali"""
        animations = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        for i in range(8):
            print(f"\r{Colors.BRIGHT_YELLOW}{animations[i % len(animations)]} HakkoAI thinking...{Colors.END}", end="", flush=True)
            time.sleep(0.12)
        print("\r" + " " * 50 + "\r", end="", flush=True)
    
    def get_mode_info(self) -> tuple:
        """Get current mode info"""
        modes = {
            "chat": ("💬", Colors.BRIGHT_GREEN, "CHAT"),
            "code": ("💻", Colors.BRIGHT_CYAN, "CODE"),
            "search": ("🔍", Colors.BRIGHT_YELLOW, "SEARCH"),
            "creative": ("🎨", Colors.BRIGHT_PURPLE, "CREATIVE")
        }
        return modes.get(self.current_mode, ("💬", Colors.BRIGHT_GREEN, "CHAT"))
    
    def send_message(self, message: str) -> Optional[str]:
        """
        Send message to OpenRouter API
        
        Args:
            message: User's message
            
        Returns:
            AI response or None
        """
        # Enhanced system prompts
        system_prompts = {
            "chat": "You are HakkoAI, a friendly and intelligent AI assistant. Be helpful, clear, and conversational.",
            "code": "You are HakkoAI in expert coding mode. Provide clean, secure, well-commented code. Include cybersecurity best practices for Kali Linux users.",
            "search": "You are HakkoAI in research mode. Provide comprehensive, well-structured information with examples.",
            "creative": "You are HakkoAI in creative mode. Help with creative writing, brainstorming, and imaginative content."
        }
        
        # Build messages
        messages = [
            {"role": "system", "content": system_prompts.get(self.current_mode, system_prompts["chat"])}
        ]
        messages.extend(self.conversation_history)
        messages.append({"role": "user", "content": message})
        
        # OpenRouter headers
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/hakkoai/terminal",
            "X-Title": "HakkoAI Terminal"
        }
        
        # Request payload
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 2048
        }
        
        try:
            self.print_thinking()
            
            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=60
            )
            
            # Handle errors
            if response.status_code == 401:
                self.print_error("Invalid API key! Check your OpenRouter key.")
                print(f"{Colors.CYAN}Get key at: https://openrouter.ai/keys{Colors.END}")
                return None
            
            if response.status_code == 402:
                self.print_error("No credits! Add credits to your OpenRouter account.")
                return None
            
            if response.status_code == 429:
                self.print_error("Rate limit exceeded! Wait a moment.")
                return None
            
            response.raise_for_status()
            result = response.json()
            
            # Extract response
            ai_response = result['choices'][0]['message']['content']
            
            # Update history
            self.conversation_history.append({"role": "user", "content": message})
            self.conversation_history.append({"role": "assistant", "content": ai_response})
            
            # Keep last 30 messages
            if len(self.conversation_history) > 30:
                self.conversation_history = self.conversation_history[-30:]
            
            self.message_count += 1
            return ai_response
            
        except requests.exceptions.Timeout:
            self.print_error("Request timed out. Check your connection.")
            return None
        except requests.exceptions.ConnectionError:
            self.print_error("Connection failed. Check your internet.")
            return None
        except Exception as e:
            self.print_error(f"Error: {e}")
            return None
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        print(f"\n{Colors.BRIGHT_GREEN}{Colors.BOLD}╔═══════════════════════════════════════╗{Colors.END}")
        print(f"{Colors.BRIGHT_GREEN}{Colors.BOLD}║  ✅ HISTORY CLEARED                  ║{Colors.END}")
        print(f"{Colors.BRIGHT_GREEN}{Colors.BOLD}╚═══════════════════════════════════════╝{Colors.END}")
        print(f"{Colors.BRIGHT_GREEN}Fresh start! Ready for new conversations.{Colors.END}\n")
    
    def show_stats(self):
        """Show session statistics"""
        duration = datetime.now() - self.session_start
        minutes = int(duration.total_seconds() / 60)
        
        print(f"\n{Colors.BRIGHT_PURPLE}{Colors.BOLD}╔═══════════════════════════════════════╗{Colors.END}")
        print(f"{Colors.BRIGHT_PURPLE}{Colors.BOLD}║  📊 SESSION STATS                    ║{Colors.END}")
        print(f"{Colors.BRIGHT_PURPLE}{Colors.BOLD}╠═══════════════════════════════════════╣{Colors.END}")
        print(f"{Colors.BRIGHT_PURPLE}{Colors.BOLD}║{Colors.END}  {Colors.BRIGHT_CYAN}⏱️  Time:{Colors.END} {minutes} min                    {Colors.BRIGHT_PURPLE}{Colors.BOLD}║{Colors.END}")
        print(f"{Colors.BRIGHT_PURPLE}{Colors.BOLD}║{Colors.END}  {Colors.BRIGHT_GREEN}💬 Messages:{Colors.END} {self.message_count}                      {Colors.BRIGHT_PURPLE}{Colors.BOLD}║{Colors.END}")
        print(f"{Colors.BRIGHT_PURPLE}{Colors.BOLD}║{Colors.END}  {Colors.BRIGHT_YELLOW}🎯 Mode:{Colors.END} {self.current_mode.upper()}                    {Colors.BRIGHT_PURPLE}{Colors.BOLD}║{Colors.END}")
        print(f"{Colors.BRIGHT_PURPLE}{Colors.BOLD}║{Colors.END}  {Colors.BRIGHT_PURPLE}🤖 Model:{Colors.END} {self.model[:20]}...  {Colors.BRIGHT_PURPLE}{Colors.BOLD}║{Colors.END}")
        print(f"{Colors.BRIGHT_PURPLE}{Colors.BOLD}╚═══════════════════════════════════════╝{Colors.END}\n")
    
    def switch_mode(self, new_mode: str):
        """Switch AI mode"""
        self.current_mode = new_mode
        emoji, color, name = self.get_mode_info()
        
        print(f"\n{color}{Colors.BOLD}╔═══════════════════════════════════════╗{Colors.END}")
        print(f"{color}{Colors.BOLD}║  {emoji} MODE: {name}                       ║{Colors.END}")
        print(f"{color}{Colors.BOLD}╚═══════════════════════════════════════╝{Colors.END}\n")
    
    def run(self):
        """Main loop - Beautiful terminal experience"""
        self.print_banner()
        
        emoji, color, name = self.get_mode_info()
        print(f"{color}{Colors.BOLD}{emoji} Mode: {name}{Colors.END}\n")
        print(f"{Colors.BRIGHT_CYAN}Ready! Type your message or command...{Colors.END}\n")
        
        while True:
            try:
                # Beautiful prompt
                emoji, color, _ = self.get_mode_info()
                prompt = f"{Colors.BOLD}{Colors.BRIGHT_BLUE}You{Colors.END} {color}{emoji}{Colors.END} {Colors.BRIGHT_CYAN}→{Colors.END} "
                user_input = input(prompt).strip()
                
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.startswith('/'):
                    cmd = user_input.lower()
                    
                    if cmd in ['/exit', '/quit', '/q']:
                        print(f"\n{Colors.BRIGHT_PURPLE}{Colors.BOLD}╔═══════════════════════════════════════╗{Colors.END}")
                        print(f"{Colors.BRIGHT_PURPLE}{Colors.BOLD}║  👋 GOODBYE FROM HAKKOAI!           ║{Colors.END}")
                        print(f"{Colors.BRIGHT_PURPLE}{Colors.BOLD}╚═══════════════════════════════════════╝{Colors.END}")
                        print(f"{Colors.BRIGHT_CYAN}Thanks for using HakkoAI! ✨{Colors.END}\n")
                        break
                    
                    elif cmd == '/clear':
                        self.clear_history()
                        continue
                    
                    elif cmd == '/stats':
                        self.show_stats()
                        continue
                    
                    elif cmd == '/help':
                        self.print_banner()
                        continue
                    
                    elif cmd in ['/chat', '/code', '/search', '/creative']:
                        self.switch_mode(cmd[1:])
                        continue
                    
                    else:
                        self.print_error(f"Unknown command: {user_input}")
                        print(f"{Colors.BRIGHT_YELLOW}💡 Type /help for commands{Colors.END}\n")
                        continue
                
                # Send to AI
                emoji, color, _ = self.get_mode_info()
                print(f"\n{Colors.BOLD}{Colors.BRIGHT_PURPLE}🤖 HakkoAI{Colors.END} {color}{emoji}{Colors.END} {Colors.BRIGHT_CYAN}→{Colors.END}\n")
                
                response = self.send_message(user_input)
                
                if response:
                    print(f"{response}\n")
                    
                    # Encouragement
                    if self.message_count % 5 == 0:
                        print(f"{Colors.BRIGHT_CYAN}✨ {self.message_count} messages! Great chat! ✨{Colors.END}\n")
                else:
                    print(f"{Colors.BRIGHT_RED}Failed to get response.{Colors.END}\n")
                
            except KeyboardInterrupt:
                print(f"\n\n{Colors.BRIGHT_YELLOW}⚠️  Interrupted!{Colors.END}")
                confirm = input(f"{Colors.BRIGHT_CYAN}Exit? (y/n): {Colors.END}").lower()
                if confirm in ['y', 'yes']:
                    print(f"\n{Colors.BRIGHT_PURPLE}{Colors.BOLD}👋 Goodbye! ✨{Colors.END}\n")
                    break
                print()
            except Exception as e:
                self.print_error(f"Error: {e}")


def main():
    """Entry point for HakkoAI"""
    
    print(f"\n{Colors.BRIGHT_CYAN}{Colors.BOLD}{'═' * 60}{Colors.END}")
    print(f"{Colors.BRIGHT_PURPLE}{Colors.BOLD}🚀 Starting HakkoAI...{Colors.END}")
    print(f"{Colors.BRIGHT_CYAN}{Colors.BOLD}{'═' * 60}{Colors.END}\n")
    
    # OPTION 1: Use environment variable (recommended)
    # ai = HakkoAI()
    
    # OPTION 2: Hardcode your API key here (for Termux/Kali convenience)
    # Uncomment and add your key:
    # **REPLACE_ME_WITH_YOUR_ACTUAL_OPENROUTER_API_KEY**
    ai = HakkoAI(api_key="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")
    
    ai.run()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n{Colors.BRIGHT_RED}{Colors.BOLD}╔═══════════════════════════════════════╗{Colors.END}")
        print(f"{Colors.BRIGHT_RED}{Colors.BOLD}║  💥 FATAL ERROR                      ║{Colors.END}")
        print(f"{Colors.BRIGHT_RED}{Colors.BOLD}╚═══════════════════════════════════════╝{Colors.END}")
        print(f"{Colors.BRIGHT_RED}{e}{Colors.END}\n")
        sys.exit(1)
