local session_log = {}
local function log_session_node(target_ip, system_os)
    local target_profile = {
        ip = target_ip
        os = system_os
        }
table.insert (session_log, target_profile)
print("[+]append node...succcessfull" .. session_log)
    end