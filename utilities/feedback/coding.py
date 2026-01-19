
class StatusCodes:
    """
    Provides an object representation of standardised HTTP-based status codes
    
    ```python
    codes = StatusCodes()
    print(codes.success)
    ```
    """
    def __str__(self): return "StatusCodes: Provides an object representation of standardised HTTP-based status codes."
    def __init__(self):

        # STATUS CODES #

        # Success
        self.success = 200

        # Security Success
        self.security_success = 228
        self.security_decrypted = 229
        self.security_encrypted = 230
        self.security_signed = 231
        self.security_verified = 232
        self.security_authenticated = 233

        # File Success
        self.file_success = 240
        self.file_created = 241
        self.file_modified = 242
        self.file_deleted = 243
        self.file_moved = 244
        self.file_copied = 245
        self.file_renamed = 246

        # User Success
        self.user_success = 280
        self.user_created = 281
        self.user_modified = 282
        self.user_deleted = 283
        self.user_moved = 284
        self.user_copied = 285
        self.user_renamed = 286

        # Program Success
        self.program_success = 290
        self.program_created = 291
        self.program_modified = 292
        self.program_deleted = 293
        self.program_moved = 294
        self.program_copied = 295
        self.program_renamed = 296
        self.program_executed = 297


        # Partial Success
        self.partial_success = 300

        self.some_fields_filled = 301
        self.some_fields_invalid = 302
        self.some_fields_unique = 303
        
        self.some_data_found = 304


        # User faults
        self.bad_request = 400
        self.unauthorized = 401
        self.forbidden = 403
        self.not_found = 404
        self.method_not_allowed = 405
        self.nice_try_mate = 406

        self.needs_privileges = 407

        # Program Faults
        self.internal_error = 500
        self.not_implemented = 501

        # Input Faults
        self.fill_all_fields = 600
        self.malformed_input = 603
        self.input_too_short = 604
        self.input_too_long = 605
        self.input_invalid = 606
        self.input_out_of_range = 607
        self.input_not_found = 608
        self.input_not_unique = 609

        self.no_such_method = 610
        self.missing_argument = 611
        self.internal_argument_not_found = 612
        self.invalid_version = 613

        # File Faults
        self.file_does_not_exist = 701
        self.file_already_exists = 702
        self.file_readonly = 703
        self.file_protected = 704
        self.file_corrupted = 705
        self.file_privileged = 706
        self.file_locked = 707
        self.file_unreadable = 708

        self.package_not_found = 801
        self.package_already_installed = 802
        self.package_not_installed = 803
        self.package_not_removed = 804
        self.package_not_updated = 805
        self.package_malformed = 806
        self.package_core = 807




        # ERROR MESSAGES #

        self.messages = {
            # Success
            self.success: "Process Successful!",

            # Security Success
            self.security_success: "Security Process Successful!",
            self.security_decrypted: "Security Process Decrypted!",
            self.security_encrypted: "Security Process Encrypted!",
            self.security_signed: "Security Process Signed!",
            self.security_verified: "Security Process Verified!",
            self.security_authenticated: "Security Process Authenticated!",

            # File Success
            self.file_success: "File Process Successful!",
            self.file_created: "File Created!",
            self.file_modified: "File Modified!",
            self.file_deleted: "File Deleted!",
            self.file_moved: "File Moved!",
            self.file_copied: "File Copied!",

            # User Success
            self.user_success: "User Process Successful!",
            self.user_created: "User Created!",
            self.user_modified: "User Modified!",
            self.user_deleted: "User Deleted!",
            self.user_moved: "User Moved!",
            self.user_copied: "User Copied!",
            self.user_renamed: "User Renamed!",

            # Program Success

            self.program_success: "Program Process Successful!",
            self.program_created: "Program Created!",
            self.program_modified: "Program Modified!",
            self.program_deleted: "Program Deleted!",
            self.program_moved: "Program Moved!",
            self.program_copied: "Program Copied!",
            self.program_renamed: "Program Renamed!",
            self.program_executed: "Program Executed!",

            # Partial Success

            self.partial_success: "Partial Success!",
            self.some_fields_filled: "Some fields were filled. Please fill in the rest.",
            self.some_fields_invalid: "Some fields were invalid. Please correct them.",
            self.some_fields_unique: "Some fields were not unique. Please change them.",
            self.some_data_found: "Some data was found. Please review it.",

            # User faults


            self.bad_request: "Your request is shambolic. Please ask us something else.",
            self.unauthorized: "Uh-oh! You're not allowed to do that. Big brother is watching you.",
            self.forbidden: "Access Forbidden. The walled garden is closed for you.",
            self.not_found: "What you've asked for could not be found by us.",
            self.method_not_allowed: "The method you have just called is not allowed. Change it up or just read documentation.",
            self.nice_try_mate: "Nice try mate. You're not getting away with that. You've been caught red-handed.",
            self.needs_privileges: "You need to be privileged to do that.",

            # Program Faults

            self.internal_error: "Whoops! I made a mistake. Or you did. Or both of us did. Either way, a cog went bust.",
            self.internal_argument_not_found: "An internally assigned argument was not found.",
            self.not_implemented: "What you have asked for isn't even a feature. Unfortunately, we can't magically let you do that yet.",

            # Input Faults

            self.fill_all_fields: "Fill in all fields bro",
            self.file_does_not_exist: "A directory location requested by the program does not exist.",
            self.file_already_exists: "A directory location requested by the program already exists.",
            self.malformed_input: "The input provided is malformed.",
            self.input_too_short: "The input provided is too short.",
            self.input_too_long: "The input provided is too long.",
            self.input_invalid: "The input provided is invalid.",
            self.input_out_of_range: "The input provided is out of range.",
            self.input_not_found: "The input provided was not found.",
            self.input_not_unique: "The input provided is not unique.",
            self.missing_argument: "An argument is missing.",
            self.invalid_version: "The version provided is invalid.",

            self.no_such_method: "The method requested does not exist.",

            # File Faults

            self.file_readonly: "The file requested is read-only.",
            self.file_protected: "The file requested is protected.",
            self.file_corrupted: "The file requested is corrupted.",
            self.file_privileged: "The file requested is privileged.",
            self.file_locked: "The file requested is locked.",
            self.file_unreadable: "The file requested is unreadable.",

            self.package_not_found: "The package requested was not found.",
            self.package_already_installed: "The package requested is already installed.",
            self.package_not_installed: "The package requested is not installed.",
            self.package_not_removed: "The package requested could not be removed.",
            self.package_not_updated: "The package requested could not be updated.",
            self.package_malformed: "The package requested is malformed.",
            self.package_core: "The package requested is a core package and cannot be tampered."
            

        }

class StatusAsMessage:
    """
    Return a string representation of the status code.

    ```python
    status_code = StatusCodes().bad_request
    error_message = StatusAsMessage(status_code)
    print(error_message)
    ```
    """
    def __init__(self, status_code):
        self.message = StatusCodes().messages[status_code]
    def __str__(self): return self.message

