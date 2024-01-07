from config import (
    CSV_FILE_PATH,
    CSV_SEPARATOR,
    CSV_ENCODING,
    RES_ENCODING,
    BAD_RECORDS_FILE_PATH,
    ERROR_STATISTICS_FILE_PATH,
)

incorrect_spc_code = 0
no_switch_id = 0

with open(CSV_FILE_PATH, "r", encoding=CSV_ENCODING) as csv:
    for line in csv:
        fields = line.split(CSV_SEPARATOR)

        if not fields[0].isdigit():
            with open(BAD_RECORDS_FILE_PATH, "a", encoding=RES_ENCODING) as bad_records:
                bad_records.write("Incorrect SPC Code: " + line)
            incorrect_spc_code += 1

        if fields[1] == "":
            with open(BAD_RECORDS_FILE_PATH, "a", encoding=RES_ENCODING) as bad_records:
                bad_records.write("No switch ID specified: " + line)
            no_switch_id += 1

    with open(ERROR_STATISTICS_FILE_PATH, "w", encoding=RES_ENCODING) as error_statistics:
        error_statistics.write("incorrect_spc_code = " +
                               str(incorrect_spc_code) +
                               "\nno_switch_id = " +
                               str(no_switch_id))
