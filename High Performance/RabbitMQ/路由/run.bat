start cmd /k "echo start receive_logs_direct1...&&python receive_logs_direct.py info warning error"
start cmd /k "echo start receive_logs_direct2...&&python receive_logs_direct.py error"
# start cmd /k "echo start emit_log_direct...&&python emit_log_direct.py error "Ops, Rush! Rush! Or it will explode.""
# start cmd /k "echo start emit_log_direct...&&python emit_log_direct.py info "just kidding. bro.""
python emit_log_direct.py warning "warning, database under the water."
python emit_log_direct.py error "fade way !__!"
python emit_log_direct.py error "Ops, Rush! Rush! Or it will explode."
python emit_log_direct.py info "just kidding. bro."
