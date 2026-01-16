"""
S-TOON Middleware Protocol
Author: Jamil Alshaer (2026)
License: MIT
"""

class STOON_Middleware:
    def __init__(self):
        # Latent Control Tokens
        self.S_START = "<|S_START|>"
        self.S_END = "<|S_END|>"

    def normalize(self, text):
        """
        Mitigates Invisible Indentation & Visual Spoofing.
        Strips: Zero-width spaces, Unicode line separators (U+2028/29).
        """
        return text.replace("\u200b", "").replace("\u200c", "").replace("\u200d")\
                   .replace("\u2028", "").replace("\u2029", "")

    def sanitize(self, text):
        """
        Mitigates Comment Masquerading & Sentinel Injection.
        """
        # 1. Neutralize Sentinel Spoofing (Attacker trying to close the tag)
        text = text.replace(self.S_END, "[BLOCKED]")
        # 2. Neutralize Comment Injection (Python/YAML style)
        text = text.replace("#", "[HASH]") 
        return text

    def protect(self, text):
        """
        Wraps input in the 'Virtual Faraday Cage'.
        This is the main function developers should call.
        """
        text = self.normalize(text)
        text = self.sanitize(text)
        return f"{self.S_START} {text} {self.S_END}"

    def validate_fail_secure(self, text, simulate_cut=False):
        """
        Mitigates Open Field Truncation.
        Ensures the closing sentinel exists before processing.
        """
        payload = self.protect(text)
        
        # Simulation for testing purposes
        if simulate_cut:
            payload = payload[:-10] 
        
        # Runtime Check
        if self.S_END not in payload:
            raise ValueError("SECURITY_EXCEPTION: Missing Closing Sentinel - Potential Truncation Attack")
        
        return payload
