local function Launch_payload()
    print("[*]Lua Engine: Attempting critical operation...")
    error("CRITICAL_NETWORK_TIMEOUT")
end

local success, report = pcall(Launch_payload)

if not success then
    print("[!]Sandbox intercepted a crash")
    print("Log Report Details:" .. report)
else
    print("[*]Operation succesfull")
end


print("[*]Initializing stealth execution...")
local success = pcall(function()
    error("SILENT_FAILURE_TARGET")
end)
print("[+]lua engine solved pasted obstacle. Status: " .. tostring(success))

