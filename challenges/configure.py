def run_with_retries(results, max_attempts=3, on_failure="skip", log=None):
    # TODO: handle the mutable default argument problem correctly —
    # do not use a mutable object like [] directly as a default value.
    # Then simulate retrying through `results` according to the rules described.
    
    if log == None:
        log = []

    for outcome in results[:max_attempts]:
        if outcome == 'success':
            log.append('success')
            break
        elif outcome == 'fail':
            if on_failure == 'log':
                log.append('attempt failed')
    
    return log

print(run_with_retries(['fail', 'fail', 'success']))
print(run_with_retries(['fail', 'fail', 'success'], on_failure='log'))
print(run_with_retries(['fail', 'fail', 'fail'], max_attempts=2))
