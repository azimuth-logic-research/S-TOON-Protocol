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
        """
        return text.replace("\u200b", "").replace("\u200c", "").replace("\u200d", "") \
                   .replace("\u2028", "").replace("\u2029", "")

    def sanitize(self, text):
        """
        Mitigates Comment Masquerading & Sentinel Injection.
        """
        text = text.replace(self.S_END, "[BLOCKED]")
        text = text.replace("#", "[HASH]") 
        return text

    def protect(self, text):
        """
        Wraps input in the 'Virtual Faraday Cage'.
        """
        text = self.normalize(text)
        text = self.sanitize(text)
        return f"{self.S_START} {text} {self.S_END}"

    def validate_fail_secure(self, text, simulate_cut=False):
        """
        Mitigates Open Field Truncation.
        """
        payload = self.protect(text)
        if simulate_cut:
            payload = payload[:-10] 
        
        if self.S_END not in payload:
            raise ValueError("SECURITY_EXCEPTION: Missing Closing Sentinel")
        
        return payload