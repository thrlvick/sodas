local function secure_handshake()
    print("[*]running handshake capture...")
    local payload = {
        msg = "WPA_HANDSKAE _TIMEOUT",
        bssid = "AB:CF:65:11:22:33",
        channel = 11
    }
    error(payload) 
end
local success, report =pcall(secure_handshake)
..argumentaion
if not success then
    print("[!]payload failure")
    print(" failure reason: " .. report.msg)
    print(" Target BSSID: " .. report.bssid)
    print(" Radio Channel: " .. report.channel)
else
    print("[+]Handshake captured!")
end
..payload sample 