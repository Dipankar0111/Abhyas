import json

questions = []

def add_q(id_num, module, q_text, options, correct_idx, explanation, difficulty="Medium"):
    questions.append({
        "id": id_num,
        "module": module,
        "question": q_text,
        "options": options,
        "correct": correct_idx,
        "explanation": explanation,
        "difficulty": difficulty
    })

# ==========================================
# CONTEST 1 (50 QUESTIONS)
# ==========================================
add_q(1, "Hardware & Storage", 
      "Aman wants faster boot times and quicker app loading on his old laptop. Which upgrade would be most effective?",
      ["Replacing his HDD with an SSD", "Buying a bigger monitor", "Getting a mechanical keyboard", "Adding external speakers"],
      0, "Boot time and app loading depend heavily on how fast the storage device can read data. SSDs are many times faster than HDDs because they have no moving parts, so switching to an SSD gives a huge speed boost.")

add_q(2, "Operating Systems",
      "Which of the following is a primary responsibility of an operating system?",
      ["Creating spreadsheets", "Managing system resources", "Designing websites", "Editing photographs"],
      1, "An operating system manages resources such as CPU time, memory, files, and input/output devices.")

add_q(3, "Computer Systems",
      "A state weather department is building a flood-warning system. Four kinds of machine are involved:\n(1) On each of two hundred rivers, a sealed waterproof box bolted to a bridge with sensor and radio.\n(2) In the district office, machines on desks for reports and calls.\n(3) In a rack room, headless machines that receive readings and answer citizen website requests.\n(4) At a national centre, one very large machine running an atmospheric simulation.\nWhich classification matches the lecture categories?",
      ["(1) personal computer, (2) embedded system, (3) supercomputer, (4) server",
       "(1) embedded system, (2) personal computer, (3) server, (4) supercomputer",
       "(1) embedded system, (2) server, (3) personal computer, (4) supercomputer",
       "(1) server, (2) personal computer, (3) embedded system, (4) supercomputer"],
      1, "(1) Dedicated bridge sensor = embedded system, (2) Office desktop = personal computer, (3) Headless multi-user data provider = server, (4) Massive parallel simulation = supercomputer.")

add_q(4, "Computer Systems",
      "Which feature of the rack-room machines - rather than their physical size or their speed - is what puts them in their category as servers?",
      ["They are kept in a locked, climate-controlled room.",
       "They have more RAM installed than the machines in the district office.",
       "They store data and provide it as a service to many other machines at the same time, over a network.",
       "They need no operating system of their own, because no person ever sits in front of them to run a program."],
      2, "A server is defined by its role: providing data, compute, or services to multiple client machines over a network.")

add_q(5, "Computer Systems",
      "The department runs a trial: on ten bridges the sealed box is replaced by an ordinary laptop. Over one monsoon the ten laptops miss 43 readings due to Windows updates, background apps, and power-saving sleep; the 190 boxes miss 2. Which conclusion do these findings support?",
      ["The laptops needed better weatherproofing.",
       "The laptops needed faster processors and more memory.",
       "The boxes are more reliable only because they were installed first.",
       "Capability a job never uses is not free. It can become a cause for which the job can fail, which is why a computer meant for one task is inefficient here."],
      3, "Capability a job never uses introduces failure modes. An embedded system dedicated to a single task eliminates unnecessary background services and sleep states.")

add_q(6, "Computer Systems",
      "Halfway through the season the department decides the river boxes should measure every ten seconds instead of thirty, and report battery level. Assuming the boxes were designed to allow it, what does the definition of a computer predict?",
      ["The behaviour can be changed by loading a new set of instructions into the hardware already on the bridge.",
       "Every box must be physically replaced, because its behaviour is fixed by the way it was built.",
       "Only the national centre's machine can be reprogrammed, since only supercomputers run software.",
       "Each box needs a GPU added before it can handle battery-level data."],
      0, "A computer is defined by its reprogrammability: you update its stored software instructions without altering its physical hardware.")

add_q(7, "Computer Systems",
      "During a flood the public website becomes unreachable for citizens. At the same time, officers in district office can read data on their screens and bridge boxes transmit normally. Which layer is the most likely point of failure, and on what reasoning?",
      ["The river boxes - they are the only machines exposed to extreme weather.",
       "The national centre's simulation - the public website exists to display simulation results.",
       "The rack-room machines' capacity to answer many simultaneous requests - the failure appears exactly where the number of users rose sharply, and not where it did not.",
       "The officers' desk machines - officers and public look at same data."],
      2, "The failure occurred exclusively where traffic spiked (the public-facing server layer), while internal office streams and sensors remained functional.")

add_q(8, "Hardware & Storage",
      "Rahul needs to carry a 2 GB project file from home to college to submit it. Which device is the most convenient choice?",
      ["The internal HDD of his desktop", "A USB flash drive", "His computer's monitor", "A RAM stick"],
      1, "A USB flash drive is small, portable, non-volatile, and plug-and-play. RAM loses data when powered off, and internal HDDs are not portable.")

add_q(9, "Operating Systems",
      "Scenario: A computer becomes almost unusable because many programs are running simultaneously and consuming available memory. Which operating system function is most directly involved in handling this situation?",
      ["Document formatting", "Screen resolution", "Memory management", "File naming"],
      2, "Memory management controls allocation, paging, swapping, and deallocation of physical and virtual memory.")

add_q(10, "Software Types",
      "Which software would normally be used to protect a computer by detecting and removing malicious programs?",
      ["Spreadsheet software", "Word processor", "Presentation software", "Antivirus utility"],
      3, "Antivirus software is a system maintenance utility that scans, identifies, and removes malicious code.")

add_q(11, "Software Types",
      "Which software would be most appropriate for calculating monthly expenses and creating charts from the results?",
      ["Antivirus utility", "Operating system", "Device driver", "Spreadsheet application"],
      3, "Spreadsheet applications (e.g., Excel, Google Sheets) are designed for mathematical calculations and chart generation.")

add_q(12, "Operating Systems",
      "A computer has enough memory and storage, but a newly connected printer does not work because the operating system cannot communicate with it. What is most likely missing?",
      ["Web browser", "File manager", "Device driver", "Spreadsheet"],
      2, "A device driver is the specialized software module that enables the OS to send commands to a specific hardware peripheral.")

add_q(13, "Hardware & Storage",
      "Why is an SSD generally faster than an HDD?",
      ["It uses larger spinning disks", "It has no moving parts", "It uses magnetic tape", "It is physically bigger in size"],
      1, "HDDs rely on mechanical spinning platters and moving heads. SSDs access data electronically via solid NAND flash chips without mechanical delay.")

add_q(14, "Hardware & Storage",
      "A clinic buys two machines. Front-desk: modest CPU, 8 GB RAM, 1 TB HDD. Imaging machine: fast CPU, 32 GB RAM, 1 TB SSD, discrete GPU. Complaint: Front-desk machine takes 2 minutes to open patient-records; imaging machine opens it in seconds. Which difference explains this?",
      ["The front-desk machine has less RAM, where programs are kept permanently.",
       "The front-desk machine reads the program off a drive with spinning platters and moving heads, while imaging reads from flash memory with no moving parts.",
       "Processor speed on its own controls how fast a program is read off a drive.",
       "The age of the drive alone determines speed."],
      1, "Loading an application into RAM is an I/O read operation from secondary storage. SSDs read files significantly faster than mechanical HDDs.")

add_q(15, "Hardware & Storage",
      "During a power cut, a receptionist lost the half-typed record she had not yet saved. Every saved record was intact when power returned. Which property of memory does this demonstrate?",
      ["The hard disk drive is volatile.",
       "The unsaved work was held inside CPU registers only.",
       "8 GB of RAM is too small to hold a patient record.",
       "Work being typed lives in RAM, which is volatile; saving copies it into secondary storage, which keeps data without power."],
      3, "Active unsaved typing resides in volatile DRAM. Saving writes the data into non-volatile secondary storage (SSD/HDD).")

add_q(16, "Hardware & Architecture",
      "The imaging machine reconstructs a scan in 40 seconds. When a technician disabled the graphics card to test something, the same scan took 26 minutes - and the CPU was untouched. Why?",
      ["The reconstruction applies the same operation repeatedly, and a GPU's thousands of small cores handle such repetitive parallel work far better than a CPU's few powerful cores.",
       "The graphics card holds its own copy of the operating system.",
       "A central processing unit cannot perform arithmetic directly.",
       "Disabling the graphics card also disabled the solid-state drive."],
      0, "Pixel image reconstruction is massively parallel arithmetic (SIMD). GPUs have thousands of lightweight arithmetic cores optimized for parallel computation.")

add_q(17, "Hardware & Storage",
      "The clinic can upgrade exactly one component on the front-desk machine to fix the 2-minute app launch time. Which upgrade should it choose?",
      ["Add a graphics card, because the program window has to be drawn.",
       "Double RAM to 16 GB, because more RAM makes the drive read faster.",
       "Replace the hard disk drive with an SSD, because the complaint is about how long data takes to be read out of long-term storage.",
       "Replace the processor, because CPU controls drive speed."],
      2, "The bottleneck is secondary storage read throughput. Replacing the mechanical HDD with an SSD solves application loading delay.")

add_q(18, "Hardware & Storage",
      "A vendor tells the clinic: 'Buy 64 GB of RAM and your staff will never again lose unsaved work in a power cut.' How should the clinic judge this claim?",
      ["Accept it - larger RAM keeps data clear of overwritten parts.",
       "Accept it - above 32 GB RAM behaves like an SSD.",
       "Reject it - RAM cannot hold a document at all.",
       "Reject it - RAM loses its contents when power is lost regardless of how much of it there is; only writing to secondary storage protects the work."],
      3, "RAM is inherently volatile regardless of its size. Data loss during power cuts can only be prevented by saving to non-volatile secondary storage.")

add_q(19, "Software Types",
      "Which pair contains only application software?",
      ["Chrome and Excel", "Windows and macOS", "Linux and Android", "BIOS and Linux"],
      0, "Chrome and Excel are end-user applications. Windows, macOS, Linux, and Android are operating systems; BIOS is system firmware.")

add_q(20, "Hardware Components",
      "A monitor is an example of which type of device?",
      ["Input device", "Storage device", "Output device", "Processing device"],
      2, "A monitor renders visual output generated by the computer's display subsystem.")

add_q(21, "Computer Systems",
      "Kiran has an orange juicer (Machine A), a digital scale updated via USB to calculate rupee prices and store 20 past weighings (Machine B), and a billing laptop (Machine C). Meera says all three are computers because they take input, process, and give output. Which property is missing?",
      ["The machine must be powered by electricity.",
       "The machine must produce output faster than a human.",
       "The machine's behaviour must be changeable by loading a different set of instructions into it.",
       "The machine must have a display."],
      2, "Reprogrammability—the ability to execute arbitrary stored instructions without changing physical hardware—distinguishes a computer from a fixed mechanical machine.")

add_q(22, "Computer Systems",
      "Applying that reprogrammability property as the test, which classification of Kiran's three machines is correct?",
      ["Machines B and C are computers; Machine A is not.",
       "Only Machine A is a computer; B and C simply move data.",
       "All three are computers, because all three take input and output.",
       "Only Machine C is a computer; A and B are single-purpose."],
      0, "Machine B (digital scale with reprogrammable firmware) and Machine C (laptop) are computers. Machine A is a purely mechanical single-purpose machine.")

add_q(23, "Computer Systems",
      "Machine B gained new behaviour - price display and a memory of past weighings - without a single physical part being replaced. What does this most directly demonstrate?",
      ["Machine B's hardware is more powerful than A's motor.",
       "What Machine B does is determined by its software, and its hardware is general enough to carry out more than one set of instructions.",
       "Machine B has more secondary storage than A.",
       "Machine B is application software rather than hardware."],
      1, "Software determines function over general-purpose programmable hardware without physical alterations.")

add_q(24, "Computer Systems",
      "The scale already beeps when weight settles. Kiran asks for a second feature: a distinct beep whenever a crate is lighter than the crate weighed immediately before it. What does this require?",
      ["An output device", "A faster processor", "A second sensor",
       "A value kept from an earlier measurement, because the machine must compare the current input against something no longer on the pan."],
      3, "Comparative temporal logic requires memory storage to preserve prior state for subsequent evaluations.")

add_q(25, "Computer Systems",
      "A student concludes: 'Machine C is a real computer and Machine B is only a gadget, because Machine C runs many different kinds of programs while Machine B runs only one.' What is the strongest objection?",
      ["Machine B also has a display.",
       "Machine C is a laptop, classified as an embedded system.",
       "How many programs a device is currently made to run is a design decision; the test is whether it can be given different instructions, and Machine B was shown to pass that test.",
       "Machine B weighs fruit faster than Machine C."],
      2, "Whether a device is restricted to one function is an operational design choice; the fundamental qualification of a computer is its programmability.")

add_q(26, "Hardware & Storage",
      "Riya's laptop slows down whenever she opens too many browser tabs, Spotify, and Word at once. Upgrading which component would help most?",
      ["Buying a bigger monitor", "Increasing the RAM", "Getting a wireless mouse", "Adding more USB ports"],
      1, "Each active application consumes RAM. When RAM is exhausted, the OS uses virtual memory disk swapping, degrading system speed. Adding RAM prevents disk thrashing.")

add_q(27, "Software Types",
      "A student wants to write assignments, calculate marks, and create presentations. Which type of software will be most useful?",
      ["Device drivers", "Firmware", "Application software", "System software"],
      2, "Productivity applications (word processors, spreadsheets, presentation software) belong to the application software category.")

add_q(28, "Software Types",
      "Which option correctly matches the software with its category?",
      ["Android — Operating system", "Linux — Application software", "Excel — System software", "Chrome — Device driver"],
      0, "Android is an operating system. Linux is an OS kernel/system, Excel is application software, and Chrome is an application.")

add_q(29, "Software Types",
      "Which of the following is a characteristic of system software?",
      ["It is used only for internet browsing", "It supports the operation of the computer", "It is designed only for presentations", "It is created only for entertainment"],
      1, "System software controls hardware devices and provides foundational operating services for user programs.")

add_q(30, "Hardware Components",
      "Speakers are considered a(n) ______ device.",
      ["Input", "Output", "Storage", "Processing"],
      1, "Speakers convert electrical sound signals from the computer into audible acoustic sound waves, making them output devices.")

add_q(31, "Hardware & Storage",
      "What does SSD stand for?",
      ["Simple Storage Device", "Solid State Drive", "System Storage Disk", "Secondary Save Drive"],
      1, "SSD stands for Solid State Drive, utilizing non-volatile semiconductor flash memory chips with zero moving parts.")

add_q(32, "Operating Systems",
      "A lab has identical hardware dual-booting Windows and Ubuntu. Why does the machine behave and appear so differently between sessions?",
      ["The operating system sits between the user and the hardware; changing it changes how the machine is presented and controlled, while the hardware itself is unchanged.",
       "Choosing an OS changes CPU clock speed.",
       "Ubuntu reconfigures the SSD into a different physical format.",
       "The two OSs divide RAM differently, which dictates screen layout."],
      0, "The operating system abstracts the underlying hardware, providing its own user interface, service layer, and process management.")

add_q(33, "Software Types",
      "Three pieces of software: a browser, a word processor, a package manager. Which grouping separates system software from application software correctly?",
      ["System software: word processor. Application software: package manager and browser.",
       "System software: package manager. Application software: browser and word processor.",
       "System software: browser and package manager. Application software: word processor.",
       "All four are application software."],
      1, "A package manager is a system utility for configuring, updating, and installing packages; browsers and word processors are user applications.")

add_q(34, "Operating Systems",
      "Bhaskar's browser needs to write a downloaded file onto the SSD. Using the three-layer stack, which account of what happens is correct?",
      ["The browser writes to the SSD directly.",
       "The SSD runs the browser.",
       "The compiler must translate the file before the OS can store it.",
       "The browser asks the operating system for the service, and the operating system, which manages the hardware, carries out the write."],
      3, "User applications execute in user space and must issue system calls to the OS kernel to interact with physical storage hardware.")

add_q(35, "Operating Systems",
      "A new printer works immediately under Windows, but prints nothing under Ubuntu although connected and powered on. What is the most reasonable explanation?",
      ["The printer hardware is incompatible with these machines.",
       "A printer can be used only by application software.",
       "The two systems need different device drivers, and the driver for this printer is present in one system's software collection but not in the other's.",
       "Ubuntu installation lacks a GPU."],
      2, "Operating systems require device-specific driver software to communicate with peripherals; Windows had the driver installed, while Ubuntu did not.")

add_q(36, "Operating Systems",
      "Bhaskar claims the Ubuntu tool to view running programs and Windows Task Manager are 'the same thing with a different name'. Which is the most defensible version of his claim?",
      ["Both are supplied by their operating system to report how the machine's resources - memory and processor time - are being used.",
       "Both are application software written by the same company.",
       "Both are device drivers.",
       "Both are compilers."],
      0, "Both tools are OS system management utilities providing real-time telemetry on active processes, CPU utilization, and RAM allocation.")

add_q(37, "Hardware & Storage",
      "A student says: 'My computer has 512 GB of RAM to store all my movies and games permanently.' What's wrong with this statement?",
      ["Nothing — RAM stores files permanently", "RAM is temporary storage", "512 GB is too little for storage", "RAM cannot hold any data at all"],
      1, "RAM is volatile temporary working memory that clears when power is disconnected. Permanent file storage requires an HDD or SSD.")

add_q(38, "Hardware Components",
      "Which of these is NOT an input device?",
      ["Keyboard", "Mouse", "Microphone", "Speaker"],
      3, "Keyboards, mice, and microphones transmit input into the computer; speakers emit sound output to the user.")

add_q(39, "Software Types",
      "Which statement best describes computer software?",
      ["Electrical signals inside a computer", "Instructions used by a computer", "Physical components of a computer", "Connections between hardware devices"],
      1, "Software consists of structured programmatic instructions and data that direct the physical hardware on how to perform operations.")

add_q(40, "Hardware & Storage",
      "Which of the following best describes a Hard Disk Drive (HDD)?",
      ["A drive with no moving parts", "A storage device with spinning disks", "A temporary memory used by the CPU", "A device used only for display"],
      1, "An HDD stores binary data magnetically on rapidly spinning platters read and written by mechanical actuator arms.")

add_q(41, "Hardware & Storage",
      "What happens to the data stored in RAM when you turn off your computer?",
      ["It stays saved forever", "It gets backed up to the cloud", "It is erased and lost", "It moves to the hard disk automatically"],
      2, "RAM is volatile memory; when electrical power ceases, the capacitive charges storing data bits dissipate, erasing its contents.")

add_q(42, "Hardware & Storage",
      "Arrange these from fastest to slowest in terms of data access speed:",
      ["HDD → SSD → RAM", "RAM → SSD → HDD", "HDD → RAM → SSD", "SSD → HDD → RAM"],
      1, "RAM operates in nanoseconds, SSD operates in microseconds, and mechanical HDD operates in milliseconds.")

add_q(43, "Operating Systems",
      "Scenario: A user saves documents inside folders and later searches for a particular file. Which operating system capability is being used?",
      ["Memory allocation", "Device installation", "File management", "Process scheduling"],
      2, "File management provides hierarchical directory organization, naming, metadata tracking, and path lookups.")

add_q(44, "Operating Systems",
      "Which statement about an operating system is correct?",
      ["It replaces all application software", "It acts as an interface between users, applications, and hardware", "It is used only to browse websites", "It is stored only on external devices"],
      1, "An OS functions as an abstraction layer and coordinator mediating between hardware components, applications, and end-users.")

add_q(45, "Software Types",
      "Which of the following is NOT an example of system software?",
      ["Microsoft Excel", "Android", "Windows", "Linux"],
      0, "Microsoft Excel is an end-user application software; Android, Windows, and Linux are operating systems.")

add_q(46, "Hardware & Storage",
      "A USB flash drive is mainly used for:",
      ["Displaying images on the screen", "Storing and transferring files", "Processing calculations", "Connecting to the internet"],
      1, "A USB flash drive is a portable, non-volatile solid-state storage medium designed for file transport and archiving.")

add_q(47, "Hardware Components",
      "Which combination correctly matches the device with its category?",
      ["Mouse → Output, Speaker → Input", "Keyboard → Input, SSD → Storage", "Monitor → Input, HDD → Output", "Speaker → Storage, RAM → Input"],
      1, "Keyboard is an input device; SSD is a secondary storage device.")

add_q(48, "Software Types",
      "Why is system software generally necessary before application software can be used effectively?",
      ["It prevents applications from accessing computer resources", "It replaces the need for computer hardware", "It provides the basic environment and services applications depend on", "It converts every application into hardware"],
      2, "System software abstracts hardware complexity and provides execution scheduling, memory allocation, and I/O channels that applications require.")

add_q(49, "Hardware Components",
      "A touchscreen on a smartphone acts as which type of device?",
      ["Storage device", "Processing device", "Input device", "Power device"],
      2, "The capacitive digitizer layer on a screen detects physical touch gestures and converts them into digital input coordinates.")

add_q(50, "Operating Systems",
      "Scenario: Riya opens several applications at the same time. Her computer needs to decide how much processor time each application receives. Which operating system function is involved?",
      ["Web browsing", "Memory allocation", "Process management", "File compression"],
      2, "Process management and the CPU scheduler allocate CPU execution time slices across active processes.")


# ==========================================
# CONTEST 2 (25 QUESTIONS)
# ==========================================
add_q(51, "Filesystem & Permissions",
      "A results file is owned by the teacher. The teacher should be able to read and write the file, while the group and all other users should only be able to read it. Nobody should have execute permission. What three-digit numeric chmod value achieves exactly this?",
      ["644", "755", "600", "777"],
      0, "Owner: Read (4) + Write (2) = 6. Group: Read (4) = 4. Others: Read (4) = 4. Combined octal permission = 644.")

add_q(52, "Operating Systems & Processes",
      "A browser tab crashes and shows an error, but other tabs continue working normally. What best explains this behavior?",
      ["The browser automatically restarts the crashed tab in the background.",
       "The other tabs had already been saved to disk before the crash.",
       "The crashed tab had not actually been running as a process.",
       "The browser isolates tab activity across processes, limiting the failure’s impact."],
      3, "Google Chrome implements multi-process architecture where each tab runs in its own child process. An unhandled exception terminates only that individual child process.")

add_q(53, "Unix Filesystem Architecture",
      "In the class demonstration, text typed in one terminal appeared in a second terminal after running echo 'hi' > /dev/pts/2. What does this illustrate?",
      ["Both terminals share one block of memory from the shell",
       "echo has a special mode for sending messages",
       "The two terminals were opened by the same parent shell",
       "Terminals are represented as files, so writing works"],
      3, "This demonstrates the Unix 'Everything is a file' model. Terminals are represented as character device files under /dev/pts/.")

add_q(54, "Filesystem & Permissions",
      "A newly created file shows -rw-r--r-- in ls -l. Which permission does the owner not have?",
      ["Read", "Execute", "Write", "The owner has all three"],
      1, "The first triplet rw- represents owner permissions: Read (r) and Write (w) are present, but Execute (x) is indicated by a dash (-).")

add_q(55, "Filesystem & Permissions",
      "A Unix-like system contains a file named hello.txt. The file is made executable with chmod +x hello.txt. It is then renamed to run_me.banana. When the user runs ./run_me.banana, it executes successfully. Why?",
      ["On Unix-like systems, execute permission is stored in the file’s permission metadata, not determined by its filename extension.",
       "The shell uses the filename extension to determine whether a file is executable.",
       "The .banana extension must be registered with the operating system as executable.",
       "Renaming a file automatically restores its default permissions."],
      0, "In Unix systems, executability is controlled by the execute bit in file inode metadata, unlike Windows where extensions like .exe define execution.")

add_q(56, "CLI & Environment",
      "The $PATH environment variable has been set to an empty string. Running ls now fails with command not found. How can ls still be run?",
      ["By giving its full path: /bin/ls", "By adding execute permission with chmod +x", "By running it through sudo instead", "By renaming the file to ls.exe first"],
      0, "The ls binary resides at /bin/ls. When $PATH is empty, automatic directory lookup fails, but specifying the absolute path executes the binary directly.")

add_q(57, "Filesystem & Permissions",
      "You keep private notes in a file that only you should be able to read and modify. No other users should have any permissions on the file. What three-digit numeric chmod permission value achieves this?",
      ["600", "644", "700", "777"],
      0, "Owner: Read (4) + Write (2) = 6. Group: None (0). Others: None (0). Numeric value = 600.")

add_q(58, "Operating Systems & Processes",
      "You need to stop a running process, but you want to give it an opportunity to close its files and exit cleanly. Which command is appropriate?",
      ["kill -9 — it terminates the process immediately.", "kill -15 — it requests that the process terminate.", "Either command — both signals behave identically.", "Neither command — a running process cannot be stopped."],
      1, "kill -15 sends SIGTERM, allowing the process to intercept the signal, execute cleanup handlers, and terminate gracefully. kill -9 sends uncatchable SIGKILL.")

add_q(59, "Filesystem & Navigation",
      "Starting at / and running cd .. repeatedly leaves you at / every time. Why?",
      ["Permission to move any higher has been denied", "cd .. is an alias that performs no action", "Directories above / exist but stay hidden", "The root directory has no parent to move into"],
      3, "The root directory / is the ultimate apex of the Unix directory hierarchy; its parent pointer .. points back to / itself.")

add_q(60, "Filesystem & Permissions",
      "Running ls -l script.sh shows -rw-r--r--. Running ./script.sh returns permission denied. Which command makes the script runnable while leaving the existing read and write permissions unchanged?",
      ["sudo ./script.sh", "chmod +x script.sh", "chmod 777 script.sh", "chown root script.sh"],
      1, "chmod +x selectively adds the execute bit across classes while preserving existing read/write bits.")

add_q(61, "Filesystem & Permissions",
      "After running chmod 754 report.sh, what permissions does the group hold?",
      ["Read, write and execute", "Read and execute", "Read only", "Read and write"],
      1, "In 754, the middle digit represents Group permissions: 5 = 4 (Read) + 1 (Execute), yielding r-x.")

add_q(62, "Filesystem Architecture",
      "Which directory is emptied automatically every time the machine reboots?",
      ["/etc", "/bin", "/tmp", "/Applications"],
      2, "/tmp is designated for temporary files and is cleared automatically during system reboot.")

add_q(63, "CLI & Shells",
      "On a current macOS system, which shell is provided as the default command-line interface?",
      ["zsh", "bash", "fish", "csh"],
      0, "macOS switched its default login shell to zsh (Z Shell) starting in macOS Catalina 10.15.")

add_q(64, "Operating Systems & Processes",
      "Why cannot Chrome read data held in VS Code's memory?",
      ["They are written in different programming languages.", "Their memory contents are encrypted separately by the OS.", "The OS gives each process an isolated virtual address space.", "They are normally scheduled on different CPU cores."],
      2, "The OS memory manager isolates processes by assigning each a distinct private virtual address space enforced by hardware MMU.")

add_q(65, "Filesystem & Permissions",
      "A classmate advises running chmod 777 whenever a permission error appears. What is the best evaluation of this advice?",
      ["Poor — it grants read, write, and execute permissions to the owner, group, and others.", "Sound — it is the quickest reliable fix available.", "Poor — a setting of 777 may only be applied by the root user.", "Sound — 777 makes a file read-only and therefore safe."],
      0, "chmod 777 strips all access security by granting write and execution rights to every user on the system.")

add_q(66, "Filesystem Commands",
      "A directory holds 100 folders named folder_1 through folder_100. Which single command removes them all?",
      ["rm -r folder_*", "rm folder_", "rm -r folder_?", "rm -r folder_1"],
      0, "The wildcard * matches any sequence of trailing characters, and -r enables recursive removal of directory trees.")

add_q(67, "Filesystem Commands",
      "Which command transfers ownership of a file to a different user?",
      ["chown", "chmod", "mv", "cp"],
      0, "chown (change owner) modifies file ownership; chmod modifies permission modes.")

add_q(68, "CLI Commands",
      "Which command reports the full filesystem path of the program that would run for a given command name?",
      ["man", "pwd", "ps", "which"],
      3, "The which command resolves an executable name against the $PATH directories and prints its absolute path.")

add_q(69, "Operating Systems & Memory",
      "A production application repeatedly dies with an out-of-memory exception under load. Based on how the OS allocates memory, what is the real remedy for the future?",
      ["Add more CPU cores so that the work finishes sooner", "Add more memory, or reduce what the app asks for", "Change the file permissions on the executable", "Terminate it with kill -9 whenever it slows"],
      1, "OOM crashes stem from memory exhaustion; adding CPU cores does not expand memory capacity. The only fix is increasing RAM/swap or optimizing application memory usage.")

add_q(70, "Unix Filesystem Architecture",
      "What does the /dev directory contain?",
      ["Files representing hardware devices", "Developer tools, compilers and libraries", "Installed applications", "System configuration files"],
      0, "/dev holds special device files representing physical and pseudo hardware devices (disks, terminals, input devices).")

add_q(71, "Filesystem Commands",
      "Which command prints the absolute path of the directory you are currently working in?",
      ["ls", "cd", "which", "pwd"],
      3, "pwd stands for Print Working Directory.")

add_q(72, "Filesystem & Permissions",
      "Permissions are given numeric values: read is 4, write is 2 and execute is 1. Which single digit grants all three at once?",
      ["3", "7", "6", "9"],
      1, "4 (Read) + 2 (Write) + 1 (Execute) = 7.")

add_q(73, "Operating Systems & Processes",
      "Assuming Google Chrome browser is a parent process, one tab of Chrome corresponds to what, in operating-system terms?",
      ["One parent process", "One child process", "One thread of the main process", "One separately installed program"],
      1, "Chrome allocates each browser tab into an isolated child process spawned from the main browser process.")

add_q(74, "Filesystem & Permissions",
      "Why does a newly created file deliberately lack execute permission?",
      ["It keeps the file smaller on disk", "It stops unvetted content being run by accident", "Only the root user is allowed to create executables", "Execute permission applies only to directories"],
      1, "Default permissions omit the execute bit as a defense-in-depth security measure against inadvertent execution of malicious or arbitrary scripts.")

add_q(75, "Operating Systems & Processes",
      "A program such as Google Chrome can be installed on a computer once. When Chrome is launched, the operating system creates one or more processes to execute it. What is the difference between a program and a process?",
      ["A program is written in source code; a process is written in machine language.",
       "A program needs the CPU; a process needs only memory.",
       "A program is a stored set of instructions; a process is an instance of that program that is currently executing, along with its execution state and allocated resources.",
       "A program belongs to the user; a process belongs to the operating system."],
      2, "A program is static code stored on disk; a process is an active runtime instance loaded into memory with execution context and system resources.")

print(f"Loaded {len(questions)} base contest questions.")
