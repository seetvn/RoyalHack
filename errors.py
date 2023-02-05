def before_after_errors(before, after):
  #More than 2 input
  if len(before) > 1:
    error_message = "Please only give 2 input to !summarize"
    return error_message

  #Wrong Format
  if len(after) not in (4,6,8,10,14) or not after.isnumeric():
    error_message = "Make sure the parameters follow this format:\n[YYYY]MM]DD]HHMM"
    return error_message

  #If only one input only messages after [after] is considered
  if not before:
    return "not error"

  #Wrong order
  if len(after) == len(before[0]) and int(after[:2]) > int(before[0][:2]):
    error_message = "The first parameter must refer to a time before the second parameter"
    return error_message
  
  return
    