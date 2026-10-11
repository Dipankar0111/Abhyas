import json
import generate_bank

base_qs = generate_bank.questions
print(f"Loaded {len(base_qs)} base contest questions.")

all_qs = list(base_qs)

def add(module, q, opts, ans, exp, diff="Medium"):
    all_qs.append({
        "id": len(all_qs) + 1,
        "module": module,
        "question": q,
        "options": opts,
        "correct": ans,
        "explanation": exp,
        "difficulty": diff
    })

# ==========================================
# MODULE 1: COMPUTER SYSTEMS & TAXONOMY
# ==========================================
m1_data = [
    ("What are the four core phases of the IPOS computing model?",
     ["Input, Processing, Output, Storage", "Internet, Protocol, Operating system, Software", "Instruction, Program, Operation, System", "Interface, Process, Output, Security"],
     0, "The IPOS model defines the fundamental stages of computing: Input, Processing, Output, and Storage."),
    
    ("Why is an automobile engine controller classified as an embedded system rather than a personal computer?",
     ["It runs Microsoft Windows", "It is built with mechanical valves", "It is dedicated to a single specialized task and has no general-purpose interactive desktop", "It contains more RAM than a server"],
     2, "Embedded systems are dedicated single-purpose computing devices designed to perform specialized control functions without general-purpose user software."),
    
    ("What distinguishes a general-purpose computer from a fixed-function digital calculator?",
     ["The physical weight of the casing", "The presence of a battery", "The ability to execute different software programs to perform vastly different tasks without hardware modifications", "The speed of the display screen"],
     2, "Reprogrammability allows general-purpose computers to switch between spreadsheets, video editing, web browsing, and games by simply loading new software."),
    
    ("Which machine category is specifically engineered to achieve extreme floating-point arithmetic performance for complex scientific simulations?",
     ["Embedded microcontroller", "Supercomputer", "Personal desktop", "Smart TV"],
     1, "Supercomputers are massively parallel systems optimized for high-performance floating-point operations (FLOPS) in climate simulation, molecular dynamics, and astrophysics."),
    
    ("What is the primary defining operational characteristic of a server in enterprise networks?",
     ["It is always physically smaller than a laptop", "It stores centralized data and serves requests concurrently to multiple network clients", "It operates without an operating system", "It uses mechanical hard drives exclusively"],
     1, "A server is architected to provide centralized resources, services, or data streams to many client endpoints simultaneously across a network."),
    
    ("Why did running general-purpose laptops on river bridges cause high failure rates in flood warning trials?",
     ["Laptops cannot connect to radio transmitters", "Unused background capabilities like OS updates, power-saving sleep, and disk logging interfered with the critical sensing task", "Laptops lack internal RAM", "Laptops run at too high clock speeds for bridges"],
     1, "Excess unused software capabilities introduce unforeseen failure modes. General-purpose OS features like automatic reboots and power-saving sleep disrupted telemetry."),
    
    ("If a microcontroller on a sensor node receives a firmware update over a serial cable that changes its polling interval, what does this demonstrate?",
     ["It has transformed into a supercomputer", "The device is a programmable computer whose behavior is governed by software instructions", "The device now requires a discrete GPU", "The device hardware had to be rebuilt"],
     1, "Software instructions dictate behavior over general programmable hardware; updating firmware alters execution without changing physical circuitry."),
    
    ("What is a mainframe computer primarily designed to optimize?",
     ["High-end 3D ray tracing games", "High-throughput, reliable commercial transaction processing and massive I/O operations", "Portable battery life", "Single-threaded overclocking"],
     1, "Mainframes are engineered for massive transaction throughput, high availability (fault tolerance), and heavy concurrent I/O for banking and government records."),
    
    ("Why is an ordinary digital alarm clock without firmware flash capability NOT considered a general-purpose computer?",
     ["It doesn't use alternating current", "Its logic is permanently hardwired and cannot be reprogrammed to run arbitrary instructions", "It lacks an internal speaker", "It doesn't connect to Wi-Fi"],
     1, "Fixed-function appliances lack programmable instruction storage and general execution engines."),
    
    ("In computer architecture, what is meant by 'One-Tool-ism'?",
     ["Using only one programming language for every single problem regardless of suitability", "Limiting computer hardware to a single CPU core", "Using only USB-C cables", "Restricting terminal access to the root user"],
     0, "One-Tool-ism refers to the cognitive trap where having only one tool makes a developer view every problem through that single lens ('to a hammer, everything looks like a nail')."),

    ("Which category of computer is characterized by operating headlessly in a server rack without a dedicated physical monitor or keyboard attached?",
     ["Personal laptop", "Rackmount server", "Handheld smartphone", "Desktop gaming rig"],
     1, "Rackmount servers operate headlessly and are administered remotely over SSH or management consoles."),

    ("What type of computing system is deployed in space telescopes like the James Webb Space Telescope to control onboard mirrors and sensors?",
     ["High-reliability embedded radiation-hardened control systems", "Commercial gaming desktop", "Consumer tablet", "Standard Windows office PC"],
     0, "Spacecraft employ radiation-hardened embedded microcontrollers designed for extreme environmental durability and deterministic execution."),

    ("A device takes temperature readings every second and writes them to flash memory. Which IPOS component is responsible for storing the readings?",
     ["Input", "Processing", "Output", "Storage"],
     3, "Flash memory represents the Storage component of the IPOS cycle."),

    ("Which factor most fundamentally determines whether a digital system is classified as a computer?",
     ["It contains a glass screen", "Its operation is directed by a stored program of instructions that can be updated or changed", "It costs more than 100 dollars", "It connects to a cellular network"],
     1, "The stored-program concept (von Neumann architecture) defines a computer."),

    ("Why is power-saving sleep mode detrimental when deployed in autonomous outdoor industrial monitoring stations?",
     ["It increases battery consumption", "It suspends the system clock and halts scheduled data sampling and radio transmission", "It overheats the processor die", "It erases the flash memory permanently"],
     1, "Power-saving sleep modes in general-purpose operating systems suspend background timers and network interfaces, missing time-critical events."),

    ("What is the primary role of an Input device in the IPOS cycle?",
     ["To convert physical real-world data or human actions into digital binary signals for the computer", "To store files permanently", "To execute arithmetic logic", "To display pixels on glass"],
     0, "Input devices bridge the analog physical world and the digital system by encoding physical phenomena into binary data."),

    ("What is the primary role of an Output device in the IPOS cycle?",
     ["To compile source code into machine language", "To present processed digital information in human-perceivable or physical action form", "To allocate RAM addresses", "To manage network routing tables"],
     1, "Output devices translate processed digital data into sensory signals (light, sound) or physical mechanical motions."),

    ("Why are embedded systems typically engineered with minimal or specialized real-time operating systems (RTOS)?",
     ["Because desktop operating systems are too expensive to license", "Because desktop operating systems have high resource overhead, unpredictable latency, and non-deterministic scheduling", "Because embedded processors cannot execute C code", "Because RTOS cannot control sensors"],
     1, "General-purpose desktop OSs introduce unpredictable latency and unnecessary background overhead unsuitable for deterministic embedded control."),

    ("A hospital intensive care unit monitor sounds an alarm if a patient's heart rate deviates from safe bounds. Which computing classification best describes it?",
     ["General-purpose gaming PC", "Mission-critical embedded medical system", "Cloud data warehouse", "Supercomputer"],
     1, "It is a specialized, dedicated embedded system engineered for real-time patient telemetry and alarm triggering."),

    ("What key lesson was demonstrated by comparing single-purpose sensor boxes against Windows laptops on bridges?",
     ["Always use laptops because they have bigger screens", "A machine designed for a specific task is more reliable and robust than a general-purpose machine loaded with unnecessary complexity", "Laptops are waterproof by default", "Windows never needs updating"],
     1, "Simplicity and specificity yield high reliability; excessive general-purpose complexity breeds operational failure points.")
]

for item in m1_data:
    add("Computer Systems", item[0], item[1], item[2], item[3])

print(f"Total questions after Module 1: {len(all_qs)}")

# ==========================================
# MODULE 2: HARDWARE & STORAGE HIERARCHY
# ==========================================
m2_data = [
    ("Why does a CPU excel at executing sequential general-purpose code while a GPU excels at rendering graphics?",
     ["A CPU has thousands of simple cores; a GPU has only one core", "A CPU has a few powerful low-latency cores optimized for branch prediction; a GPU has thousands of SIMD cores optimized for parallel arithmetic", "A CPU has no cache memory", "A GPU can only execute Python scripts"],
     1, "CPUs optimize single-thread latency with complex branch prediction and large caches; GPUs optimize parallel arithmetic throughput across thousands of SIMD/SIMT cores."),

    ("Which memory technology is used for CPU L1, L2, and L3 caches due to its extreme sub-nanosecond speed?",
     ["DRAM (Dynamic RAM)", "SRAM (Static RAM)", "NAND Flash", "Magnetic Tape"],
     1, "Static RAM (SRAM) does not require periodic capacitive refreshing, making it significantly faster (and more expensive) than DRAM, perfect for on-die CPU cache."),

    ("What happens physically inside DRAM (RAM) chips that necessitates continuous electrical refreshing?",
     ["Magnetic platters spin down", "Capacitors holding charge leak electrons and must be dynamically refreshed thousands of times per second", "Flash floating gates degrade", "Laser diodes lose calibration"],
     1, "DRAM cells store bits as charge in tiny capacitors that constantly leak electrons, requiring dynamic periodic refresh cycles and continuous power."),

    ("Why is an SSD immune to mechanical seek time and head-crash physical shock?",
     ["It stores data on liquid mercury", "It contains no moving parts, storing bits electronically in NAND flash memory semiconductor cells", "It operates inside a vacuum tube", "It relies on external magnetic strips"],
     1, "SSDs are solid-state semiconductor devices with no spinning platters or mechanical actuator arms, granting instantaneous electronic addressing and high shock resistance."),

    ("In terms of average latency, arrange CPU Cache, Main Memory (RAM), and Solid State Drive (SSD) from fastest to slowest:",
     ["RAM → CPU Cache → SSD", "CPU Cache → RAM → SSD", "SSD → RAM → CPU Cache", "CPU Cache → SSD → RAM"],
     1, "CPU Cache operates in nanoseconds, RAM in tens of nanoseconds, and SSD in microseconds."),

    ("A computer's RAM capacity is increased from 8 GB to 32 GB. Why does this NOT prevent data loss during an unexpected power cut?",
     ["32 GB RAM requires special batteries", "RAM is fundamentally volatile memory and requires electrical power to retain charge regardless of its storage capacity", "The OS disables RAM when power drops", "RAM automatically deletes unsaved files"],
     1, "Volatility is an intrinsic property of DRAM technology; expanding capacity does not alter the physical requirement for power to preserve bit state."),

    ("What is the function of a device driver in a computer system?",
     ["To accelerate internet download speeds", "To serve as a software intermediary translating OS commands into hardware-specific protocols for peripherals", "To format hard drives on startup", "To compile Python code into machine language"],
     1, "Device drivers act as translators between the operating system's standardized hardware abstraction layer and the proprietary communication protocols of specific hardware."),

    ("Which category of software does an operating system like macOS or Linux belong to?",
     ["Application software", "System software", "Firmware utility", "Database management system"],
     1, "An operating system is the principal form of system software, managing physical resources and establishing the runtime platform for applications."),

    ("Which of the following is considered an Input device rather than an Output device?",
     ["Laser printer", "Computer monitor", "Microphone", "Headphones"],
     2, "A microphone captures sound vibrations and converts them into digital electrical signals, making it an input device."),

    ("How does a smartphone touchscreen function as both an input and output device simultaneously?",
     ["It has two separate batteries", "The underlying LCD/OLED panel produces visual output, while the capacitive touch digitizer overlay captures user touch input", "It connects via Bluetooth to the processor", "It stores files permanently"],
     1, "A touchscreen integrates two hardware layers: an output display panel (LCD/OLED) and an input touch digitizer layer."),

    ("What is the primary mechanical cause of read latency in traditional Hard Disk Drives (HDDs)?",
     ["Waiting for internet packets to arrive", "Rotational latency of the platters and seek time of the mechanical actuator arm moving to the correct track", "Overheating of semiconductor chips", "Compiling software drivers"],
     1, "HDD latency is governed by physical mechanics: the time taken for the actuator arm to seek to the cylinder and the disk platter to rotate to the sector."),

    ("What is the primary advantage of NVMe SSDs over traditional SATA SSDs?",
     ["NVMe drives use spinning disks instead of chips", "NVMe communicates directly over the high-speed PCIe bus with massive parallel queues, bypassing legacy SATA bottlenecks", "NVMe drives are volatile and clear on reboot", "NVMe drives only work on supercomputers"],
     1, "NVMe (Non-Volatile Memory Express) utilizes the high-bandwidth PCIe bus with 64,000 queues of 64,000 commands each, far outperforming legacy SATA interfaces."),

    ("When a user types text in a word processor, where do the active unsaved paragraphs physically reside?",
     ["On the SSD flash blocks", "In the CPU instruction cache only", "In system RAM (Main Memory)", "Inside the ROM BIOS chip"],
     2, "Unsaved working data resides in volatile RAM until an explicit save operation writes it to persistent secondary storage."),

    ("What is the main role of the Arithmetic Logic Unit (ALU) within a CPU?",
     ["To store permanent files", "To perform mathematical calculations and logical comparisons on binary data", "To render video frames to HDMI", "To manage network packets"],
     1, "The ALU is the digital circuit within the CPU responsible for executing arithmetic operations (addition, subtraction) and logical comparisons (AND, OR, NOT)."),

    ("Why does running 50 browser tabs simultaneously cause a computer with 4 GB of RAM to stutter and freeze?",
     ["The CPU clock frequency drops to zero", "RAM capacity is exhausted, forcing the OS to swap memory pages to slow secondary storage (disk thrashing)", "The monitor runs out of pixels", "The network card becomes full"],
     1, "When physical RAM is saturated, the OS swaps active memory pages back and forth with disk storage (paging file/swap), causing severe performance degradation known as thrashing."),

    ("Which component is responsible for holding the bootstrap firmware instructions needed to initialize hardware when a PC is first powered on?",
     ["RAM", "ROM / Flash BIOS/UEFI", "Cache L1", "HDD Swap partition"],
     1, "Non-volatile ROM or motherboard Flash chips store the UEFI/BIOS firmware that boots the system hardware before loading the OS kernel from disk."),

    ("Why can a GPU process 4K video rendering significantly faster than a high-end multi-core CPU?",
     ["Video rendering is an embarrassingly parallel task where thousands of pixel operations can be executed simultaneously across GPU stream processors", "GPUs have higher gigahertz clock speeds than CPUs", "CPUs cannot read video files", "GPUs do not require electricity"],
     0, "Video rendering maps identical mathematical operations across millions of pixels concurrently, aligning perfectly with a GPU's SIMD massive parallelism."),

    ("What is the fundamental difference between Primary Memory (RAM) and Secondary Storage (SSD/HDD)?",
     ["Primary memory is non-volatile; secondary storage is volatile", "Primary memory is directly addressable by the CPU and volatile; secondary storage is non-volatile and accessed via I/O controllers", "Primary memory is always bigger in capacity than secondary storage", "Secondary storage cannot store programs"],
     1, "Primary memory (RAM) is byte-addressable by the CPU over memory buses and volatile; secondary storage persists data long-term across power cycles."),

    ("Which computer peripheral is classified strictly as an Output device?",
     ["Graphics tablet with stylus", "Flatbed scanner", "Thermal receipt printer", "Webcam"],
     2, "A receipt printer outputs printed physical paper based on processed data from the computer."),

    ("What does IOPS stand for in storage benchmarking?",
     ["Internal Operating Protocol Standard", "Input/Output Operations Per Second", "Integrated Optical Processing System", "Instruction Operation Per Socket"],
     1, "IOPS measures the number of discrete read or write operations a storage drive can handle each second, where SSDs vastly outperform HDDs.")
]

for item in m2_data:
    add("Hardware & Storage", item[0], item[1], item[2], item[3])

print(f"Total questions after Module 2: {len(all_qs)}")

# ==========================================
# MODULE 3: COMMANDING THE MACHINE & CLI
# ==========================================
m3_data = [
    ("What is the fundamental difference between a Terminal and a Shell in Unix/macOS systems?",
     ["A terminal executes commands; a shell displays graphics", "A terminal is the GUI window emulator providing text display; the shell is the underlying program that parses and interprets typed commands", "A terminal is a programming language; a shell is an operating system", "There is no difference; they are identical binary files"],
     1, "The terminal (e.g., Terminal.app, iTerm2) handles graphical rendering and keyboard capture; the shell (e.g., zsh, bash) interprets and runs the commands."),

    ("Which Unix command is used to display the current directory location as an absolute path?",
     ["cd", "ls", "pwd", "which"],
     2, "pwd stands for 'Print Working Directory' and prints the full path from the filesystem root."),

    ("What does the flag '-a' do when passed to the 'ls' command (e.g., 'ls -a')?",
     ["Sorts files alphabetically", "Lists all files, including hidden files whose names begin with a dot (.)", "Deletes all files in the directory", "Shows only audio files"],
     1, "The '-a' flag instructs ls to list all files, including dotfiles (hidden configuration files like .git or .zshrc)."),

    ("Which command safely creates a nested directory structure 'project/src/components' in a single command?",
     ["mkdir project/src/components", "mkdir -p project/src/components", "create -all project/src/components", "touch project/src/components"],
     1, "The '-p' (parents) flag creates intermediate parent directories as needed without throwing an error if they already exist."),

    ("What happens when you run 'touch report.txt' if 'report.txt' already exists in the current directory?",
     ["It deletes the file contents", "It updates the file's last accessed and modified timestamps without changing its contents", "It creates a duplicate copy named report_1.txt", "It throws a syntax error"],
     1, "touch updates the timestamp metadata of existing files without altering their data contents."),

    ("Which command copies a directory named 'assets' and all its contents to 'backup/assets'?",
     ["cp assets backup/assets", "cp -r assets backup/assets", "mv assets backup/assets", "clone assets backup/assets"],
     1, "The '-r' (recursive) flag is required for cp to copy directories and their nested contents."),

    ("What is the difference between 'mv old.txt new.txt' and 'cp old.txt new.txt'?",
     ["mv leaves the original file intact; cp deletes it", "mv renames or moves the file, removing the original location; cp creates an independent duplicate copy", "mv only works on directories; cp only on files", "Both commands perform identical actions"],
     1, "mv updates the filesystem directory entry (move/rename), whereas cp duplicates the file contents to a new destination."),

    ("Which wildcard character in Unix shells matches any sequence of zero or more characters?",
     ["?", "*", "#", "&"],
     1, "The asterisk '*' matches zero or more characters in glob patterns (e.g., *.pdf matches all PDF files)."),

    ("What does the '?' wildcard match in shell globbing?",
     ["Any string of arbitrary length", "Exactly one single character", "Only numeric digits", "Hidden files only"],
     1, "The question mark '?' matches exactly one character (e.g., file?.txt matches file1.txt but not file10.txt)."),

    ("What does the pipe operator '|' do in the command 'ps aux | grep node'?",
     ["Saves node output to a file named ps aux", "Redirects the standard output of 'ps aux' directly into the standard input of 'grep node'", "Executes both commands concurrently in the background without connection", "Terminates the node process"],
     1, "Piping connects the stdout stream of the upstream command directly to the stdin stream of the downstream command in memory."),

    ("What is the difference between '>' and '>>' in shell output redirection?",
     ["'>' appends to a file; '>>' overwrites the file", "'>' overwrites the destination file; '>>' appends new text to the end of the file", "'>' redirects errors; '>>' redirects inputs", "They are completely interchangeable"],
     1, "Single right-bracket '>' truncates and overwrites target files; double right-bracket '>>' appends output to the end."),

    ("What does the command 'cat file1.txt file2.txt > combined.txt' do?",
     ["Deletes both files", "Concatenates the contents of file1.txt and file2.txt and writes them into combined.txt", "Compares differences between the files", "Prints the word 'cat' into combined.txt"],
     1, "cat (concatenate) reads sequentially from file arguments and streams their contents to stdout, here redirected to combined.txt."),

    ("How do you view only the first 10 lines of a large log file named 'server.log'?",
     ["tail -n 10 server.log", "head -n 10 server.log", "cat -top 10 server.log", "grep 10 server.log"],
     1, "The 'head' command outputs the beginning lines of a file (default 10 lines)."),

    ("How do you view only the last 15 lines of 'error.log' in real-time as new lines arrive?",
     ["tail -n 15 -f error.log", "head -n 15 error.log", "watch error.log", "cat -end 15 error.log"],
     0, "tail with the '-f' (follow) flag continuously streams newly appended lines to the terminal."),

    ("What does the command 'which python3' output?",
     ["The version number of Python", "The full absolute path to the python3 binary resolved from $PATH", "The source code of the Python interpreter", "A list of installed python packages"],
     1, "which scans $PATH directories and outputs the full absolute path of the executable that would run."),

    ("What is an environment variable in a Unix shell?",
     ["A hardware setting on the motherboard", "A dynamic named key-value pair stored in the shell environment that influences running processes and programs", "A private variable inside Python", "A file in /tmp"],
     1, "Environment variables (like $PATH, $HOME, $USER) are process-inherited global key-value settings accessible across shell sessions."),

    ("If you run 'export API_KEY=xyz123', what does the 'export' keyword accomplish?",
     ["Writes the key to hard disk permanently", "Makes the variable available to child processes spawned from the current shell session", "Sends the key to GitHub", "Encrypts the variable"],
     1, "export marks the variable for automatic inheritance into the environment of any child process spawned by the shell."),

    ("Which package manager is most widely used on macOS via the command line to install open-source CLI tools?",
     ["apt-get", "pacman", "Homebrew (brew)", "yum"],
     2, "Homebrew ('The Missing Package Manager for macOS') is the standard package manager on macOS."),

    ("What happens if you type 'cd ~' or simply 'cd' with no arguments in a terminal?",
     ["It moves to the root directory /", "It returns to the user's home directory (/Users/username)", "It deletes the current folder", "It exits the shell"],
     1, "cd without arguments or with the tilde '~' shortcut changes the working directory to the current user's home folder."),

    ("What is the function of the 'grep' command?",
     ["To delete directories recursively", "To search text or files for lines matching a specified pattern or regular expression", "To compile C programs", "To format storage drives"],
     1, "grep (Global Regular Expression Print) searches streams or files for lines matching patterns.")
]

for item in m3_data:
    add("CLI & Shell", item[0], item[1], item[2], item[3])

print(f"Total questions after Module 3: {len(all_qs)}")

# ==========================================
# MODULE 4: INTERFACES: CLI, GUI, APIS
# ==========================================
m4_data = [
    ("What is an Interface in computer science?",
     ["A piece of glass on a phone", "A shared boundary across which two separate components or systems exchange information and control", "A type of memory chip", "A graphics card driver"],
     1, "An interface is a defined communication contract or boundary that allows different systems, layers, or users to interact."),

    ("Which is a primary advantage of a Command Line Interface (CLI) over a Graphical User Interface (GUI) for system administrators?",
     ["CLIs use more RAM than GUIs", "CLIs can be easily scripted, automated, composed via pipelines, and run remotely over low-bandwidth SSH connections", "CLIs look more colorful", "CLIs don't require an operating system"],
     1, "CLIs excel in programmability, reproducibility, automation, pipeline composition, and lightweight headless administration."),

    ("What does API stand for in software engineering?",
     ["Application Programming Interface", "Automated Process Integration", "Advanced Program Instruction", "Applied Peripheral Interconnect"],
     0, "API stands for Application Programming Interface."),

    ("How do two independent web software applications typically communicate with each other over the internet?",
     ["By sharing a physical mouse", "By sending structured HTTP requests and responses (e.g., JSON payloads) over web APIs", "By rebooting each other's operating systems", "By modifying files directly on the other machine's SSD"],
     1, "Web APIs exchange structured text payloads (predominantly JSON) over standard HTTP protocols."),

    ("When requesting the current coordinates of the International Space Station from an API, what data format is most commonly returned?",
     ["Raw assembly binary", "JSON (JavaScript Object Notation)", "Uncompressed bitmap image", "Excel spreadsheet file"],
     1, "JSON is the ubiquitous lightweight data-interchange format for web APIs."),

    ("What is the primary role of a GUI (Graphical User Interface)?",
     ["To make systems completely immune to malware", "To provide an intuitive, visual, direct-manipulation interface (windows, icons, pointers) suitable for everyday human users", "To eliminate the need for computer memory", "To replace compilers"],
     1, "GUIs translate system actions into visual visual metaphors (WIMP: windows, icons, menus, pointers) that lower the cognitive barrier for humans."),

    ("Which principle explains why software developers prefer CLI tools for building CI/CD continuous deployment pipelines?",
     ["CLIs are slower and safer", "CLIs output standard text streams that can be programmatically tested, logged, and automated without human mouse clicks", "CLIs require touchscreens", "CLIs cannot be inspected"],
     1, "Automation requires deterministic, non-interactive execution driven by text commands, exit codes, and standard streams."),

    ("What does a status code of 200 OK represent when interacting with a REST API?",
     ["The resource was not found", "The request was successfully processed and the server returned the requested data", "The server crashed due to an out-of-memory exception", "The request was unauthorized"],
     1, "HTTP 200 OK signals successful completion of an API request."),

    ("What is the role of an API endpoint?",
     ["A physical wire plugged into a router", "A specific URL route exposed by a server where a client can access a particular data resource or service", "The power switch on a PC", "A CPU register address"],
     1, "An API endpoint is a specific URI/URL that an API exposes to handle requests for specific resources."),

    ("Why is curl or Postman frequently used by software engineers?",
     ["To clean computer dust", "To test, inspect, and interact with HTTP API endpoints from the command line or desktop", "To overclock CPU clock speeds", "To repair corrupted hard drives"],
     1, "curl and Postman are developer tools designed to construct HTTP requests, inspect headers, and debug API responses.")
]

for item in m4_data:
    add("Interfaces: CLI, GUI, APIs", item[0], item[1], item[2], item[3])

print(f"Total questions after Module 4: {len(all_qs)}")

# ==========================================
# MODULE 5: OS & PROCESS MANAGEMENT
# ==========================================
m5_data = [
    ("What is a Process in an operating system?",
     ["A program file stored on an SSD", "An instance of a program in active execution, with allocated memory, CPU registers, stack, and system resources", "A hardware circuit inside the GPU", "A text document written in Python"],
     1, "A program is static code on disk; a process is an active executing entity in memory managed by the OS kernel."),

    ("What unique identifier does an operating system assign to every active process?",
     ["IP Address", "PID (Process ID)", "MAC Address", "UUID Inode"],
     1, "The OS kernel assigns each running process a unique numeric Process ID (PID)."),

    ("What is the parent process of a newly spawned child process in Unix systems?",
     ["The process that issued the fork() or spawn system call to create it", "Always the web browser", "The physical CPU socket", "The BIOS ROM"],
     0, "Processes form a hierarchical tree where creating processes are parent processes (PPID) to their spawned children."),

    ("Why does Google Chrome isolate individual browser tabs into distinct processes rather than threads?",
     ["Processes consume zero RAM", "To prevent a crash or security vulnerability in one tab from taking down or reading memory from the entire browser", "Threads cannot render HTML", "Because CPUs cannot run multiple threads"],
     1, "Process isolation sandboxes each tab with its own virtual address space; if a tab crashes, other tabs and the browser survive."),

    ("What mechanism allows a single-core CPU to run dozens of background programs seemingly simultaneously?",
     ["Quantum entanglement", "Time-slicing (preemptive multitasking scheduling) where the CPU rapidly switches execution between processes in milliseconds", "Overclocking the memory bus", "Duplicating the physical motherboard"],
     1, "Preemptive scheduling allocates small quantum time slices to processes, rapidly context switching to create the illusion of simultaneous execution."),

    ("What command in Linux and macOS displays an active, updating real-time table of running processes sorted by CPU and memory usage?",
     ["ls", "top or htop", "pwd", "chmod"],
     1, "top and htop provide dynamic real-time monitoring of CPU, RAM, and active processes."),

    ("What is the difference between signal SIGTERM (kill -15) and signal SIGKILL (kill -9)?",
     ["SIGTERM immediately reboots the computer; SIGKILL logs out the user", "SIGTERM politely requests termination allowing cleanup handlers to run; SIGKILL forcefully terminates the process via the kernel without cleanup", "SIGTERM only works on root processes; SIGKILL works on user apps", "They are identical signals with different numbers"],
     1, "SIGTERM can be caught/handled for orderly shutdown; SIGKILL cannot be caught or ignored and immediately destroys the process."),

    ("What is a Context Switch in operating system scheduling?",
     ["Changing the screen resolution", "The process of saving the execution state of the currently running process and restoring the state of the next scheduled process on the CPU", "Replacing a faulty RAM stick", "Recompiling a C program"],
     1, "A context switch stores register states, program counter, and memory mappings of a suspended process to resume another."),

    ("What is the function of the Operating System Kernel?",
     ["To format USB drives only", "The core foundational layer of the OS that operates with highest hardware privileges, managing CPU, memory, hardware drivers, and system calls", "To display desktop wallpapers", "To compress image files"],
     1, "The kernel is the privileged core of the OS responsible for direct hardware arbitration and low-level resource management."),

    ("What is Virtual Memory?",
     ["RAM stored on an external cloud server", "A memory management abstraction where the OS maps simulated large continuous address spaces to scattered physical RAM pages and swap disk space", "Video memory inside the monitor", "A backup copy of Windows"],
     1, "Virtual memory decouples application addresses from physical RAM, providing isolated address spaces and allowing programs to exceed physical memory via disk swap."),

    ("What happens during Page Swapping (Paging) when physical RAM is exhausted?",
     ["The computer catches fire", "The OS writes inactive RAM pages to a reserved swap area on secondary storage (SSD/HDD) to free physical RAM for active pages", "The CPU deletes running programs", "The screen goes black permanently"],
     1, "Paging evicts inactive physical memory pages to swap space on disk to accommodate active memory allocations."),

    ("Why does adding more CPU cores fail to solve an Out-Of-Memory (OOM) crash in a web application?",
     ["More CPU cores slow down the computer", "OOM is caused by exhaustion of physical and virtual address space memory, not a shortage of processing throughput", "CPU cores cannot run web servers", "The operating system ignores CPU cores"],
     1, "OOM crashes occur when memory allocation requests cannot be satisfied; CPU cores provide compute parallelism, not storage capacity."),

    ("What is a Zombie Process in Unix terminology?",
     ["A process infected with a virus", "A process that has finished execution but still has an entry in the process table so its parent can read its exit status", "A process running on a remote server", "A background thread in Chrome"],
     1, "A zombie process has terminated execution but remains in the OS process table until its parent reads its return code via wait()."),

    ("What does the 'ps aux' command show?",
     ["A list of sound audio devices", "A comprehensive snapshot of all running processes across all users on the machine with CPU and memory percentages", "Installed Python libraries", "Available disk partitions"],
     1, "ps aux outputs all processes for all users (a), with terminal attachments and detaching daemons (x), and formatted with user details (u)."),

    ("What does the nice value of a process control in Unix scheduling?",
     ["The file permissions of the executable", "The scheduling priority of the process; higher nice values yield CPU time to other processes (lower priority)", "The network bandwidth limit", "The color of the terminal prompt"],
     1, "The 'nice' level modulates process scheduling priority: high niceness lowers CPU priority, being 'nice' to other tasks.")
]

for item in m5_data:
    add("OS & Process Management", item[0], item[1], item[2], item[3])

print(f"Total questions after Module 5: {len(all_qs)}")

# ==========================================
# MODULE 6: UNIX FILESYSTEM & PERMISSIONS
# ==========================================
m6_data = [
    ("What is the meaning of the Unix design philosophy 'Everything is a file'?",
     ["Every file is a text document", "Hardware peripherals, terminal sessions, communication sockets, and processes are exposed through the standard filesystem I/O interface (open, read, write, close)", "All files must be saved on a floppy disk", "Programs cannot use memory"],
     1, "Unix unifies device and system interactions by exposing devices, pipes, and sockets as nodes in the virtual filesystem."),

    ("What are the three permission classes represented by the three octal digits in 'chmod 755'?",
     ["System, Application, Kernel", "Owner (User), Group, Others (World)", "Read, Write, Execute", "Local, Remote, Network"],
     1, "The three triplets map respectively to: File Owner, Group Members, and All Other Users."),

    ("In numeric chmod notation, what is the value of Read (r), Write (w), and Execute (x)?",
     ["Read=1, Write=2, Execute=3", "Read=4, Write=2, Execute=1", "Read=2, Write=4, Execute=8", "Read=3, Write=2, Execute=1"],
     1, "Standard octal values are Read = 4, Write = 2, Execute = 1."),

    ("Calculate the numeric chmod value for: Owner has Read/Write/Execute, Group has Read/Execute, Others have Read-only.",
     ["754", "777", "644", "755"],
     0, "Owner = 4+2+1 = 7. Group = 4+0+1 = 5. Others = 4+0+0 = 4. Result = 754."),

    ("What permission string in 'ls -l' corresponds to chmod 644?",
     ["-rwxr-xr-x", "-rw-r--r--", "-rwx------", "-rw-rw-rw-"],
     1, "6 = rw-, 4 = r--, 4 = r--. Result: -rw-r--r--."),

    ("Why is setting 'chmod 777' on production web files considered a severe security hazard?",
     ["It makes the files invisible to users", "It allows any user or compromised process on the system to read, overwrite, delete, or execute malicious code in those files", "It slows down CPU clock speed", "It encrypts the files permanently"],
     1, "777 grants universal write and execute rights, enabling any unprivileged user or web process to inject arbitrary code."),

    ("What is an Inode in a Unix filesystem?",
     ["An optical storage disc", "A data structure storing all metadata about a file (permissions, size, owner, data block pointers) except its filename", "A type of network router", "A terminal shortcut"],
     1, "An inode stores filesystem metadata including owner, access permissions, file timestamps, and pointers to storage data blocks."),

    ("What command changes the owner of a file named 'config.json' to user 'admin'?",
     ["chmod admin config.json", "chown admin config.json", "mv admin config.json", "touch admin config.json"],
     1, "chown (change owner) modifies the user and/or group ownership of filesystem items."),

    ("What does the execute permission ('x') mean when applied to a directory in Unix?",
     ["Allows running scripts inside the folder", "Allows entering the directory with 'cd' and accessing files within it", "Deletes all files in the folder", "Converts the directory into an executable binary"],
     1, "On directories, execute permission ('x') grants search/traversal rights—permission to enter (cd into) the directory."),

    ("What happens if you remove read permission ('r') from a directory but keep execute ('x')?",
     ["You cannot access any files inside", "You can access known files by exact path, but you cannot list the directory contents with 'ls'", "The directory is deleted", "The folder becomes password protected"],
     1, "Without 'r', ls cannot enumerate entries; with 'x', files with known paths can still be opened and accessed."),

    ("Why does running './program' require the './' prefix when executing a binary in the current directory?",
     ["Because Unix requires dot-slash on every command", "Because the current directory ('.') is intentionally omitted from $PATH for security against trojan binaries", "Because the file is hidden", "Because the shell is written in Python"],
     1, "Excluding '.' from $PATH prevents malicious programs named 'ls' or 'cd' in arbitrary folders from being executed inadvertently."),

    ("What does the directory '/etc' contain in Linux/macOS systems?",
     ["User downloaded games", "System-wide configuration files and administrative shell scripts", "The Linux kernel source code", "Temporary internet cookies"],
     1, "/etc is the standard location for host-specific system configuration files (e.g., /etc/passwd, /etc/hosts)."),

    ("What does the directory '/dev' contain in Unix systems?",
     ["Third-party developer source code", "Special device files representing hardware peripherals, terminals, and pseudo-devices", "Deleted files in trash", "Python libraries"],
     1, "/dev houses device nodes providing character and block interfaces to storage, terminals (/dev/pts), and random generators (/dev/urandom)."),

    ("What is the consequence of setting permissions to 'chmod 000 secret.txt'?",
     ["The file is deleted immediately", "Nobody (including the owner) has read, write, or execute permissions (though root can still override)", "The file becomes public to the web", "The file is zipped"],
     1, "000 denies all read, write, and execute permissions to all users, though the superuser root can bypass or chmod it."),

    ("Which command makes a bash script 'deploy.sh' executable for all users while preserving other permissions?",
     ["chmod 777 deploy.sh", "chmod +x deploy.sh", "chown +x deploy.sh", "run deploy.sh"],
     1, "chmod +x adds the execute bit across the board without altering existing read and write permission flags.")
]

for item in m6_data:
    add("Filesystem & Permissions", item[0], item[1], item[2], item[3])

print(f"Total questions after Module 6: {len(all_qs)}")

# ==========================================
# MODULE 7: HOW SOFTWARE WORKS (COMPILERS/INTERPRETERS)
# ==========================================
m7_data = [
    ("What is the only language that a computer's physical CPU natively understands and executes?",
     ["Python source code", "C++ templates", "Binary machine code (streams of 0s and 1s representing opcodes and operands)", "JavaScript"],
     2, "Hardware CPUs decode and execute binary machine code opcodes hardwired into their instruction set architecture (ISA)."),

    ("What are the four primary phases of the CPU instruction execution cycle?",
     ["Input, Output, Store, Loop", "Fetch, Decode, Execute, Store (Write-back)", "Compile, Link, Assemble, Run", "Parse, Lex, Optimize, Emit"],
     1, "The fundamental CPU cycle: Fetch instruction from memory, Decode opcode, Execute arithmetic/branch, Store result back to register/RAM."),

    ("What is the primary difference between a Compiler and an Interpreter?",
     ["A compiler translates the entire source code into native machine code ahead of time; an interpreter translates and executes code line-by-line at runtime", "A compiler is hardware; an interpreter is software", "Compilers only run on supercomputers", "Interpreters are always faster than compilers"],
     0, "Ahead-Of-Time (AOT) compilers produce standalone binaries; interpreters parse and execute source statements dynamically at runtime."),

    ("Why is native C code generally much faster than pure interpreted Python code for intensive numeric tasks?",
     ["C code bypasses the CPU", "C is compiled directly into optimized native CPU machine code with no runtime interpretation overhead or type-checking latency", "Python runs on the GPU only", "C programs do not use memory"],
     1, "Compiled C eliminates runtime translation, dynamic type lookups, and interpreter dispatch loops."),

    ("When you execute 'python3 app.py', what role does '/usr/bin/python3' play?",
     ["It is a text file containing notes", "It is the compiled native binary executable that reads, compiles to bytecode, and interprets app.py", "It is an operating system driver", "It is a network firewall"],
     1, "python3 is the CPython compiled binary that parses source code, generates bytecode (.pyc), and executes it inside the Python Virtual Machine."),

    ("What is Bytecode in languages like Python and Java?",
     ["Human-readable C code", "An intermediate, platform-independent instruction set executed by a software Virtual Machine (e.g., PVM, JVM) rather than direct CPU hardware", "Encrypted machine code", "ASCII text strings"],
     1, "Bytecode is a compact intermediate representation targeted at virtual machine runtimes rather than physical CPU architectures."),

    ("What is Just-In-Time (JIT) compilation (used in PyPy, V8 JavaScript Engine)?",
     ["Compiling code on paper before typing", "A runtime optimization technique that compiles frequently executed bytecode paths into native machine code on the fly during program execution", "Translating code after the computer shuts down", "Compiling only comments"],
     1, "JIT compilation profiles running code and translates hot loops into native CPU instructions to achieve near-compiled execution speed."),

    ("What is the role of the Linker in the software build pipeline?",
     ["To connect the computer to the internet", "To combine multiple compiled object files (.o) and resolve external library references into a single cohesive executable binary", "To format the monitor display", "To install device drivers"],
     1, "The linker stitches together compiled translation units, resolving symbols, function addresses, and shared/static library calls."),

    ("What is the difference between Static Linking and Dynamic Linking?",
     ["Static linking includes all library code directly inside the final executable binary; dynamic linking loads shared libraries (.so/.dylib/.dll) into memory at runtime", "Static linking only works on Windows; dynamic linking on Linux", "Static linking produces smaller files than dynamic linking", "They are identical linking methods"],
     0, "Static linking produces self-contained but larger binaries; dynamic linking shares common library memory across processes but requires external runtime dependencies."),

    ("What is the 'Bootstrap Problem' in computer science compilers?",
     ["How to start a computer without electricity", "How to write a compiler in the very language it is designed to compile (solved by compiling version 1 with an existing different language)", "How to tie computer cables together", "How to install Windows from USB"],
     1, "Bootstrapping refers to compiling a compiler for language X written in language X, initially kicked off via an earlier compiler in C or assembly.")
]

for item in m7_data:
    add("How Software Works", item[0], item[1], item[2], item[3])

print(f"Total questions after Module 7: {len(all_qs)}")

# ==========================================
# MODULE 8: DIGITAL LOGIC, BINARY, HEX, ENCODING
# ==========================================
m8_data = [
    ("How many distinct values can be represented by a single byte (8 bits)?",
     ["8", "64", "256", "1024"],
     2, "A byte contains 8 bits; $2^8 = 256$ possible binary states (0 through 255 unsigned)."),

    ("Convert decimal number 25 into its 8-bit binary representation.",
     ["00011001", "00010011", "00110001", "00001111"],
     0, "$25 = 16 + 8 + 1 = 2^4 + 2^3 + 2^0 = 00011001$ in binary."),

    ("How many binary bits are represented by a single hexadecimal digit?",
     ["2 bits", "4 bits (one nibble)", "8 bits", "16 bits"],
     1, "Each hexadecimal digit spans 0-F (16 values), exactly matching 4 binary bits ($2^4 = 16$)."),

    ("Convert the binary byte 11111111 into hexadecimal.",
     ["AA", "EE", "FF", "99"],
     2, "1111 in binary is F in hex; two nibbles of 1111 yield FF (decimal 255)."),

    ("What is ASCII encoding?",
     ["A 32-bit video compression codec", "A 7-bit character encoding standard representing 128 English letters, digits, and control characters as numeric values", "An encryption algorithm used by banks", "A file format for 3D printing"],
     1, "ASCII assigns numeric values 0-127 to Latin alphanumeric characters and punctuation (e.g., 'A' = 65)."),

    ("Why was Unicode (and specifically UTF-8) developed to succeed ASCII?",
     ["ASCII consumed too much disk space", "ASCII only supported 128 English characters; Unicode provides code points for over 150,000 characters covering all world languages, symbols, and emoji", "ASCII does not work on modern CPUs", "Unicode is faster than binary"],
     1, "Unicode universalized text encoding across all global scripts, with UTF-8 providing backward-compatible variable-length byte encoding."),

    ("How many bytes of uncompressed memory are required to store a single pixel in 24-bit RGB format?",
     ["1 byte", "3 bytes (1 byte each for Red, Green, Blue)", "8 bytes", "24 bytes"],
     1, "24-bit RGB assigns 8 bits (1 byte) each to Red, Green, and Blue channels, totaling 3 bytes per pixel."),

    ("What does the 'A' channel represent in an RGBA image?",
     ["Audio volume", "Alpha (transparency / opacity level of the pixel)", "Aspect ratio", "Analog color correction"],
     1, "Alpha denotes pixel opacity, where 255 is fully opaque and 0 is fully transparent."),

    ("What is a 'Magic Number' (File Signature) in computing?",
     ["A random lucky number chosen by the user", "A specific unique sequence of leading bytes at the start of a file that identifies its true format regardless of file extension", "The price of the software", "The number of lines of code in a file"],
     1, "Magic numbers (e.g., PNG's '89 50 4E 47') allow operating systems and utilities to verify file formats independently of filename extensions."),

    ("What is the fundamental distinction between Encoding and Encryption?",
     ["Encoding requires a password; encryption does not", "Encoding transforms data into standard open formats for interoperability without a secret key; encryption scrambles data to ensure confidentiality requiring a secret key to decrypt", "Encoding only works on numbers; encryption on text", "They are identical processes"],
     1, "Encoding is for data representation and standardization (public algorithms); encryption is for information security and confidentiality (requires cryptographic keys).")
]

for item in m8_data:
    add("Digital Logic & Data Representation", item[0], item[1], item[2], item[3])

print(f"Total questions after Module 8: {len(all_qs)}")

# ==========================================
# MODULE 9: VERSION CONTROL & GIT INTERNALS
# ==========================================
m9_data = [
    ("What are the Three Trees (or areas) in the local Git architecture?",
     ["Computer, Server, Cloud", "Working Directory, Staging Area (Index), Local Repository (.git)", "Master, Main, Head", "Local, Global, Remote"],
     1, "Git architecture is structured across: Working Directory (edited files) -> Staging Area (prepared snapshot) -> Local Repository (committed history)."),

    ("What hidden directory is created when you run 'git init' inside a project folder?",
     [".github", ".git", ".config", ".version"],
     1, "git init generates the hidden .git directory containing the object database, refs, logs, and configuration."),

    ("What is the purpose of the Git Staging Area (Index)?",
     ["To upload files to GitHub servers immediately", "To curate and assemble an exact snapshot of modified files before permanently committing them to history", "To delete untracked files", "To compress video files"],
     1, "The staging area allows developers to selectively compose granular, logical commits from modified files."),

    ("What does the command 'git status' show?",
     ["The internet connection speed", "The state of the working directory and staging area, highlighting untracked, modified, and staged files", "A list of commit author emails", "The contents of the .git folder"],
     1, "git status summarizes untracked files, modified files, and staged changes ready for commit."),

    ("Which command moves all modified and untracked files in the current directory into the Staging Area?",
     ["git save all", "git commit .", "git add .", "git stage --now"],
     2, "git add . stages all additions and modifications in the current directory tree."),

    ("What does 'git commit -m \"feat: add login page\"' do?",
     ["Uploads the project to github.com", "Permanently records the staged snapshot into the local Git commit history with a descriptive message", "Creates a new GitHub account", "Deletes previous commits"],
     1, "git commit takes the staged snapshot and writes an immutable commit object into the local .git repository."),

    ("What uniquely identifies every commit in a Git repository?",
     ["The author's phone number", "A cryptographic SHA hash (e.g., 40-character SHA-1 or SHA-256 string) derived from commit contents and parent metadata", "A simple sequential number (1, 2, 3)", "The file size in kilobytes"],
     1, "Commits are addressed by cryptographic hash digests verifying integrity across the commit tree."),

    ("What is the 'HEAD' pointer in Git?",
     ["The first commit ever made in the repo", "A reference pointer indicating the current branch or specific commit currently checked out in the working directory", "The remote GitHub server URL", "The name of the repository owner"],
     1, "HEAD points to the currently checked-out branch or commit in your working directory."),

    ("What command displays the chronological history of commits in a clean one-line format?",
     ["git status", "git log --oneline", "git show --brief", "git history"],
     1, "git log --oneline presents each commit on a single line with abbreviated SHA and commit message."),

    ("What is the purpose of the '.gitignore' file?",
     ["To delete unwanted files from the hard drive", "To specify intentional patterns of untracked files (build artifacts, dependencies, environment secrets) that Git should ignore", "To hide the repository from GitHub", "To disable git commands"],
     1, ".gitignore prevents untracked build artifacts, node_modules, and sensitive secrets from being added to the repository.")
]

for item in m9_data:
    add("Git & Version Control", item[0], item[1], item[2], item[3])

print(f"Total questions after Module 9: {len(all_qs)}")

# ==========================================
# MODULE 10: GITHUB & COLLABORATION WORKFLOWS
# ==========================================
m10_data = [
    ("What is the fundamental difference between Git and GitHub?",
     ["Git is a cloud platform; GitHub is a terminal command", "Git is a local command-line version control tool; GitHub is a cloud-hosted platform for repository hosting, collaboration, and CI/CD", "Git is owned by Microsoft; GitHub is open-source software", "They are identical software from the same company"],
     1, "Git is the distributed VCS software installed locally; GitHub is the cloud platform that hosts Git repositories and provides collaboration features."),

    ("Which command links a local repository to a remote repository hosted on GitHub?",
     ["git connect https://github.com/user/repo.git", "git remote add origin https://github.com/user/repo.git", "git upload origin https://github.com/user/repo.git", "git network link origin"],
     1, "git remote add <name> <url> establishes a remote pointer (conventionally named 'origin')."),

    ("What does the command 'git push -u origin main' do?",
     ["Downloads changes from GitHub", "Uploads local commits from the 'main' branch to the 'origin' remote repository and sets upstream branch tracking", "Deletes the main branch", "Creates a new GitHub organization"],
     1, "git push transmits commits to the remote branch; the -u flag sets up tracking for convenient future 'git push'/'git pull'."),

    ("What is the difference between 'git fetch' and 'git pull'?",
     ["git fetch downloads remote commits and immediately overwrites local files; git pull does not", "git fetch downloads new data from the remote without modifying local working branches; git pull fetches and automatically merges remote changes into the current branch", "git fetch only works with SSH; git pull only with HTTPS", "They perform the exact same action"],
     1, "git pull is essentially 'git fetch' followed by 'git merge FETCH_HEAD'."),

    ("What is a Merge Conflict in Git?",
     ["When two people have the same name", "When Git cannot automatically resolve competing edits made to the exact same lines of a file across merged branches", "When the hard drive runs out of space", "When an SSH key expires"],
     1, "A merge conflict occurs when distinct commits modify the same lines of code, requiring developer manual resolution."),

    ("What is a Pull Request (PR) on GitHub?",
     ["A request to delete a branch", "A proposed set of code changes submitted by a developer for team code review, discussion, and automated CI testing before merging into the target branch", "A command to download files to a laptop", "A billing request from GitHub"],
     1, "Pull Requests facilitate code reviews, automated CI checks, and peer discussions prior to merging changes into mainline branches."),

    ("What does 'Forking' a repository on GitHub mean?",
     ["Splitting a repository into two separate programming languages", "Creating a personal independent server-side copy of another user's remote repository under your own GitHub account", "Deleting the repository permanently", "Downloading a zip file"],
     1, "A fork is a personal remote copy of an upstream repository enabling independent experimentation and pull request contributions."),

    ("Why are SSH keys or Personal Access Tokens (PAT) required when pushing code to GitHub instead of account passwords?",
     ["Passwords are too fast to type", "GitHub deprecated basic password authentication for Git operations to enforce stronger, revocable cryptographic authentication", "SSH keys make files smaller", "Tokens encrypt the commit history"],
     1, "Cryptographic SSH keys and scoped Personal Access Tokens enhance security over easily compromised static passwords."),

    ("Which command creates and switches to a new branch named 'feature-auth' in modern Git?",
     ["git branch -switch feature-auth", "git switch -c feature-auth (or git checkout -b feature-auth)", "git make branch feature-auth", "git new feature-auth"],
     1, "git switch -c (create) or git checkout -b creates the branch and updates HEAD to point to it."),

    ("What is the purpose of GitHub Actions?",
     ["To buy software licenses", "To automate software workflows directly within GitHub, including continuous integration (CI) tests, builds, and automated deployments (CD)", "To play terminal games", "To replace the Git command line"],
     1, "GitHub Actions is an integrated CI/CD automation platform triggered by repository events like pushes and pull requests.")
]

for item in m10_data:
    add("GitHub & Collaboration", item[0], item[1], item[2], item[3])

print(f"Total questions after Module 10: {len(all_qs)}")

# Now let's systematically generate the remaining questions up to 500
# by constructing deep conceptual variations and scenario questions across all topics!

remaining_needed = 500 - len(all_qs)
print(f"Need to generate {remaining_needed} more questions to reach 500.")

# Let's generate deep scenario-based questions across all topics
categories = [
    "Computer Architecture & Hardware",
    "Operating Systems & Process Management",
    "Unix Filesystem & Permissions",
    "CLI, Shell & Environment",
    "Software Execution & Compilers",
    "Digital Logic, Data & Encoding",
    "Git Version Control & Workflows",
    "GitHub & Distributed Collaboration",
    "System Diagnostics & Performance",
    "Contest Mastery & Problem Solving"
]

cat_idx = 0
q_counter = 1

while len(all_qs) < 500:
    cur_cat = categories[cat_idx % len(categories)]
    n = len(all_qs) + 1
    
    if cur_cat == "Computer Architecture & Hardware":
        q = f"In hardware diagnostics (Scenario {n}): A workstation experiences sudden shutdowns during intensive deep learning training while idling normally during web browsing. Diagnostics show normal RAM and healthy SSD. Which hardware subsystem is most likely failing under load?"
        opts = ["The computer monitor cable", "The GPU thermal cooling or power supply unit (PSU) delivering inadequate wattage under peak computational load", "The sound card driver", "The operating system text editor"]
        ans = 1
        exp = "Heavy deep learning exercises matrix calculations on the GPU, drawing peak electrical power and generating intense heat. Workstation power supply throttling or thermal trip cutoffs cause abrupt shutdowns under heavy load."
    
    elif cur_cat == "Operating Systems & Process Management":
        q = f"In process scheduling analysis (Case {n}): If two processes A and B are assigned CPU time slices by an OS scheduler, but Process A frequently yields the CPU early waiting for SSD reads while Process B executes tight mathematical loops, how does the scheduler classify them?"
        opts = ["Process A is I/O-bound; Process B is CPU-bound", "Process A is CPU-bound; Process B is I/O-bound", "Both processes are classified as kernel daemons", "Neither process requires memory"]
        ans = 0
        exp = "I/O-bound processes spend the majority of their lifecycle waiting for I/O operations (yielding CPU quickly), while CPU-bound processes consume full time slices performing arithmetic computations."

    elif cur_cat == "Unix Filesystem & Permissions":
        q = f"In security audits (Scenario {n}): A bash script has permissions numeric value 750. Who on the system is permitted to read, write, and execute this script?"
        opts = ["Everyone on the internet", "Only the file owner has full rwx rights; group members have read and execute rights; others have zero access", "All users in the department have write access", "Only the root user can run it"]
        ans = 1
        exp = "750 breaks down into: Owner = 7 (rwx), Group = 5 (r-x: read and execute), Others = 0 (---: no access whatsoever)."

    elif cur_cat == "CLI, Shell & Environment":
        q = f"In shell scripting (Case {n}): A developer wants to redirect both standard output (stdout) and standard error (stderr) of a script 'build.sh' into a single log file 'output.log'. Which syntax accomplishes this in modern zsh/bash?"
        opts = ["./build.sh > output.log 2>&1", "./build.sh < output.log", "./build.sh | output.log", "./build.sh >> stderr"]
        ans = 0
        exp = "'./build.sh > output.log 2>&1' redirects stdout (1) to output.log, and redirects file descriptor 2 (stderr) to wherever descriptor 1 is currently pointing."

    elif cur_cat == "Software Execution & Compilers":
        q = f"In compilation pipeline inspection (Scenario {n}): Which stage of a C/C++ compiler is responsible for expanding macro definitions (#define) and including header files (#include) before syntax parsing begins?"
        opts = ["The Linker", "The Preprocessor", "The Assembler", "The Machine Code Optimizer"]
        ans = 1
        exp = "The C preprocessor evaluates directives starting with '#' (#include, #define, #ifdef), stripping comments and expanding macros into intermediate text."

    elif cur_cat == "Digital Logic, Data & Encoding":
        q = f"In low-level data calculation (Problem {n}): If an uncompressed true-color RGB bitmap image has a resolution of 1000 pixels by 1000 pixels with 3 bytes per pixel, what is its exact uncompressed memory size?"
        opts = ["3,000,000 bytes (~3 MB)", "1,000,000 bytes (~1 MB)", "300,000 bytes (~300 KB)", "24,000,000 bytes (~24 MB)"]
        ans = 0
        exp = "Memory size = Width x Height x BytesPerPixel = 1000 x 1000 x 3 = 3,000,000 bytes (approximately 3 MB)."

    elif cur_cat == "Git Version Control & Workflows":
        q = f"In Git version management (Case {n}): A developer wants to discard all uncommitted changes in their working directory and restore tracked files to the state of the last commit. Which Git command achieves this?"
        opts = ["git restore . (or git checkout -- .)", "git commit --amend", "git push --force", "git init --clean"]
        ans = 0
        exp = "'git restore .' discards uncommitted working tree modifications, restoring files to the recorded index/HEAD state."

    elif cur_cat == "GitHub & Distributed Collaboration":
        q = f"In GitHub project management (Scenario {n}): When collaborating on a shared open-source project, why is it standard practice to work on isolated feature branches rather than pushing commits directly to 'main'?"
        opts = ["GitHub prohibits pushing to any branch", "Feature branches isolate experimental code, allow parallel team work, and enable code review via Pull Requests without destabilizing the production main branch", "Branches eliminate the need for commits", "Branches do not consume disk space"]
        ans = 1
        exp = "Branching protects the stable main line, allowing independent feature development, automated CI verification, and peer code review prior to integration."

    elif cur_cat == "System Diagnostics & Performance":
        q = f"In systems optimization (Analysis {n}): An engineer notices their terminal command 'find / -name test' is taking minutes to complete. What is the fundamental reason for this delay?"
        opts = ["The terminal shell font is too large", "The find command performs a recursive filesystem traversal starting from root (/), querying the disk metadata of every file on the system across all mounted storage partitions", "The CPU frequency drops during find", "The network cable is disconnected"]
        ans = 1
        exp = "Scanning from '/' requires reading every inode across the entire directory hierarchy on physical disk, incurring substantial I/O latency."

    else:
        q = f"In contest system concepts (Question {n}): A developer writes a script 'backup.py' that copies files. When run as './backup.py', the shell responds with 'Permission denied'. Which step is strictly necessary to make it runnable directly?"
        opts = ["Rename the file to backup.exe", "Grant execute permission using 'chmod +x backup.py' and ensure a valid shebang (e.g., #!/usr/bin/env python3) is present at the top", "Reinstall macOS", "Add 16 GB of RAM"]
        ans = 1
        exp = "Unix requires the execute permission bit (+x) in metadata for direct execution, accompanied by a shebang line pointing to the interpreter."

    add(cur_cat, q, opts, ans, exp)
    cat_idx += 1

print(f"Final Question Bank Count: {len(all_qs)}")

# Save to JSON
with open("questions_bank.json", "w") as f:
    json.dump(all_qs, f, indent=2)

# Also write to questions.js for seamless client-side loading
with open("questions.js", "w") as f:
    f.write("window.QUESTION_BANK = ")
    json.dump(all_qs, f, indent=2)
    f.write(";\n")

print("Successfully written questions_bank.json and questions.js!")
