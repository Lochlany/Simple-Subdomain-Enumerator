import socket

domain = input("Enter base domain (like google.com): ")
subdomains = ["dev", "mail", "api", "admin", "test", "blog"]
    
print(f"Scanning {domain} for subdomains...")
    
for sub in subdomains:
    sub_domain = f"{sub}.{domain}"
    try:
        ip = socket.gethostbyname(sub_domain)
        print(f"[+] Found: {sub_domain} -> {ip}")
    except:
        pass