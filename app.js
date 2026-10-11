/* --------------------------------------------------------------------------
   ABHYAS MULTI-SUBJECT PROCTORED ASSESSMENT ENGINE
   Subjects: S&AI, Maths, PSP, Physics
   Authentication: Student Sign In & Profile Management
   -------------------------------------------------------------------------- */

(function () {
  'use strict';

  // Config
  const BATCH_SIZE = 50;
  const DEFAULT_DURATION_SECONDS = 45 * 60; // 45 minutes

  // Active Subject State
  let currentSubjectKey = 'sai'; // 'sai', 'maths', 'psp', 'physics'
  let currentBatchIndex = 0;
  let currentTestQuestions = [];
  let userAnswers = {};
  let reviewFlags = {};
  let visitedQuestions = new Set();
  let currentQuestionIndex = 0;
  
  // Dashboard Filtering
  let dashboardFilter = 'all';

  // Timer & Proctoring
  let timerInterval = null;
  let remainingSeconds = DEFAULT_DURATION_SECONDS;
  let violationCount = 0;
  let lastViolationTime = 0;
  let testStartTime = 0;
  let violationAutoSubmitTimer = null;
  let mediaStream = null;
  let isTestActive = false;
  let isReviewFilter = 'all';

  // Storage Keys
  const AUTH_KEY = 'abhyas_auth_candidate_v1';

  // Authentication Data
  function getAuthUser() {
    try {
      const data = localStorage.getItem(AUTH_KEY) || localStorage.getItem('nirman_auth_candidate_v1');
      return data ? JSON.parse(data) : {
        name: 'Kumar Dipankar Sahoo',
        roll: 'E26B07F0588',
        email: 'kumar.sahoo@student.edu',
        isLoggedIn: true
      };
    } catch (e) {
      return { name: 'Kumar Dipankar Sahoo', roll: 'E26B07F0588', email: 'kumar.sahoo@student.edu', isLoggedIn: true };
    }
  }

  function saveAuthUser(user) {
    try {
      localStorage.setItem(AUTH_KEY, JSON.stringify(user));
    } catch (e) {}
  }

  // Student-specific progress key generator so every student has their own data
  function getStudentProgressKey(customUser) {
    const user = customUser || getAuthUser();
    if (!user || !user.isLoggedIn) return 'abhyas_progress_guest';
    const id = (user.roll || user.email || user.name || 'guest')
      .trim()
      .toLowerCase()
      .replace(/[^a-z0-9_-]/g, '_');
    return `abhyas_progress_student_${id}`;
  }

  // Progress Storage per subject (strictly isolated per candidate)
  function getProgressData() {
    try {
      const key = getStudentProgressKey();
      const data = localStorage.getItem(key);
      if (data) {
        return JSON.parse(data);
      }

      // Preserve Kumar's legacy data if logging in as Kumar Dipankar Sahoo
      const currentUser = getAuthUser();
      if (currentUser && (currentUser.roll === 'E26B07F0588' || currentUser.name.toLowerCase().includes('kumar'))) {
        const legacy = localStorage.getItem('abhyas_progress_v2') || localStorage.getItem('nirman_progress_v1');
        if (legacy) {
          localStorage.setItem(key, legacy);
          return JSON.parse(legacy);
        }
      }

      // Fresh student profile starts with 0 attempts, 0 XP, full pending pool
      return {
        sai: { completedBatches: {}, totalXp: 0 },
        maths: { completedBatches: {}, totalXp: 0 },
        psp: { completedBatches: {}, totalXp: 0 },
        physics: { completedBatches: {}, totalXp: 0 }
      };
    } catch (e) {
      return {
        sai: { completedBatches: {}, totalXp: 0 },
        maths: { completedBatches: {}, totalXp: 0 },
        psp: { completedBatches: {}, totalXp: 0 },
        physics: { completedBatches: {}, totalXp: 0 }
      };
    }
  }

  function saveProgressData(data) {
    try {
      const key = getStudentProgressKey();
      localStorage.setItem(key, JSON.stringify(data));
    } catch (e) {}
  }

  // DOM Elements
  const signinView = document.getElementById('signin-view');
  const subjectsView = document.getElementById('subjects-view');
  const dashboardView = document.getElementById('dashboard-view');
  const testView = document.getElementById('test-view');
  const resultView = document.getElementById('result-view');
  const testHeaderStatus = document.getElementById('test-header-status');
  
  const navChangeSubject = document.getElementById('nav-change-subject');
  const userHeaderSignedIn = document.getElementById('user-header-signedin');
  const userHeaderSignedOut = document.getElementById('user-header-signedout');
  const headerUserName = document.getElementById('header-user-name');

  const timerDisplay = document.getElementById('timer-display');
  const violationCountEl = document.getElementById('violation-count');
  const paletteGrid = document.getElementById('palette-grid');
  const optionsList = document.getElementById('options-list');
  const questionText = document.getElementById('question-text');
  const currentQPill = document.getElementById('current-q-pill');
  const currentQCode = document.getElementById('current-q-code');
  const currentQModule = document.getElementById('current-q-module');
  const flagBtn = document.getElementById('flag-btn');
  const flagBtnText = document.getElementById('flag-btn-text');
  const paletteSummary = document.getElementById('palette-summary');

  // Initialize Application
  window.addEventListener('DOMContentLoaded', () => {
    checkAuthAndInit();
    setupSecurityListeners();
  });

  // --------------------------------------------------------------------------
  // AUTHENTICATION MANAGEMENT
  // --------------------------------------------------------------------------
  function checkAuthAndInit() {
    const user = getAuthUser();
    if (!user || !user.isLoggedIn) {
      showSignInScreen();
    } else {
      updateUserHeader(user);
      showSubjectSelection();
    }
  }

  function updateUserHeader(user) {
    headerUserName.textContent = user.name;
    document.getElementById('subject-candidate-name').textContent = user.name;
    document.getElementById('subject-candidate-roll').textContent = user.roll;
    userHeaderSignedIn.style.display = 'flex';
    userHeaderSignedOut.style.display = 'none';
  }

  window.showSignInScreen = function () {
    isTestActive = false;
    hideAllViews();
    signinView.style.display = 'block';
    userHeaderSignedIn.style.display = 'none';
    userHeaderSignedOut.style.display = 'block';
    navChangeSubject.style.display = 'none';
  };

  window.handleSignInSubmit = function (e) {
    e.preventDefault();
    const name = document.getElementById('input-student-name').value.trim() || 'Candidate';
    const roll = document.getElementById('input-roll-no').value.trim() || 'REG-001';
    const email = document.getElementById('input-email').value.trim() || 'candidate@campus.edu';

    const user = { name, roll, email, isLoggedIn: true };
    saveAuthUser(user);
    updateUserHeader(user);
    showSubjectSelection();
  };

  window.signOutUser = function () {
    if (confirm('Sign out from candidate session?')) {
      const user = getAuthUser();
      user.isLoggedIn = false;
      saveAuthUser(user);
      showSignInScreen();
    }
  };

  // --------------------------------------------------------------------------
  // SUBJECT SELECTION PORTAL
  // --------------------------------------------------------------------------
  window.showSubjectSelection = function () {
    isTestActive = false;
    clearInterval(timerInterval);
    stopCameraStream();

    hideAllViews();
    subjectsView.style.display = 'block';
    testHeaderStatus.style.display = 'none';
    const mainNav = document.getElementById('main-nav-links');
    if (mainNav) mainNav.style.display = 'flex';
    navChangeSubject.style.display = 'none';
    document.getElementById('nav-portal-btn').classList.add('active');
  };

  window.selectSubject = function (subjectKey) {
    currentSubjectKey = subjectKey;
    const subject = window.ALL_SUBJECTS[subjectKey];
    if (!subject) return;

    hideAllViews();
    dashboardView.style.display = 'block';
    const mainNav = document.getElementById('main-nav-links');
    if (mainNav) mainNav.style.display = 'flex';
    navChangeSubject.style.display = 'inline-block';
    document.getElementById('nav-portal-btn').classList.remove('active');

    // Update Dashboard Header
    document.getElementById('dash-subject-bracket').textContent = `[ ${subject.name.toUpperCase()} REGISTRY ]`;
    document.getElementById('dash-subject-code-tag').textContent = subject.tag;
    document.getElementById('dash-subject-title').textContent = `${subject.name} Assessment Hub`;
    document.getElementById('dash-subject-desc').textContent = subject.desc;

    initSubjectDashboard();
  };

  function hideAllViews() {
    signinView.style.display = 'none';
    subjectsView.style.display = 'none';
    dashboardView.style.display = 'none';
    testView.style.display = 'none';
    resultView.style.display = 'none';
    testHeaderStatus.style.display = 'none';
  }

  // --------------------------------------------------------------------------
  // SUBJECT DASHBOARD & TEST FEED
  // --------------------------------------------------------------------------
  function initSubjectDashboard() {
    const subject = window.ALL_SUBJECTS[currentSubjectKey];
    const progress = getProgressData();
    const subProgress = progress[currentSubjectKey] || { completedBatches: {}, totalXp: 0 };

    const totalQuestions = subject.total;
    const totalBatches = Math.ceil(totalQuestions / BATCH_SIZE);

    let totalAttempted = 0;
    let earnedXp = subProgress.totalXp || 0;

    for (let b = 0; b < totalBatches; b++) {
      if (subProgress.completedBatches[b]) {
        totalAttempted += subProgress.completedBatches[b].total;
      }
    }

    const pending = totalQuestions - totalAttempted;

    document.getElementById('stat-total-qs').textContent = totalQuestions;
    document.getElementById('stat-completed-qs').textContent = totalAttempted;
    document.getElementById('stat-remaining-qs').textContent = Math.max(0, pending);
    document.getElementById('stat-xp').textContent = earnedXp;

    // Pick first uncompleted batch
    let nextUnseen = 0;
    while (nextUnseen < totalBatches && subProgress.completedBatches[nextUnseen]) {
      nextUnseen++;
    }
    if (nextUnseen >= totalBatches) nextUnseen = 0;
    currentBatchIndex = nextUnseen;

    renderSubjectBatchGrid();
  }

  window.setDashboardFilter = function(filter) {
    dashboardFilter = filter;
    document.querySelectorAll('.filter-pills-row .filter-pill').forEach(btn => {
      btn.classList.remove('active');
    });
    const activeBtn = document.getElementById(`filter-btn-${filter}`);
    if (activeBtn) activeBtn.classList.add('active');
    renderSubjectBatchGrid();
  };

  window.filterBatchGrid = function() {
    renderSubjectBatchGrid();
  };

  function renderSubjectBatchGrid() {
    const subject = window.ALL_SUBJECTS[currentSubjectKey];
    const progress = getProgressData();
    const subProgress = progress[currentSubjectKey] || { completedBatches: {} };
    const totalBatches = Math.ceil(subject.total / BATCH_SIZE);

    const grid = document.getElementById('tests-batch-grid');
    grid.innerHTML = '';

    const searchVal = (document.getElementById('test-search-input')?.value || '').toLowerCase().trim();

    const saiTopics = [
      "Hardware Architecture, Storage & IPOS (Contest 1)",
      "Unix Filesystem, chmod, Processes & Signals (Contest 2)",
      "Computer Systems & Mission-Critical Machine Types",
      "Memory Hierarchy: CPU Cache, RAM Volatility & SSDs",
      "Commanding the Machine: Shell Navigation & $PATH",
      "The Interface Spectrum: CLI, GUI & REST APIs",
      "Operating Systems: Process Isolation & Multitasking",
      "Unix Philosophy: Everything is a File & Permissions",
      "Compilers vs. Interpreters: Machine Code & Runtimes",
      "Git Architecture & Distributed GitHub Collaboration"
    ];

    for (let i = 0; i < totalBatches; i++) {
      const isCompleted = !!subProgress.completedBatches[i];
      const result = subProgress.completedBatches[i];

      if (dashboardFilter === 'completed' && !isCompleted) continue;
      if (dashboardFilter === 'pending' && isCompleted) continue;

      const topicName = (currentSubjectKey === 'sai') ? saiTopics[i] : `${subject.name} Comprehensive Core Evaluation`;

      if (searchVal && !topicName.toLowerCase().includes(searchVal) && !(`test ${i+1}`).includes(searchVal)) {
        continue;
      }

      const startQ = i * BATCH_SIZE + 1;
      const endQ = Math.min((i + 1) * BATCH_SIZE, subject.total);

      const card = document.createElement('div');
      card.className = 'nirman-card test-item-card';

      let statusPill = isCompleted
        ? `<span class="tag-pill yellow-pill">SCORE: ${result.score}/${result.total} (${Math.round((result.score/result.total)*100)}%)</span>`
        : `<span class="tag-pill neutral-pill">READY</span>`;

      card.innerHTML = `
        <div class="test-left-info">
          <div class="test-header-tags">
            <span class="tag-pill yellow-pill">${subject.code}-SET-${(i + 1).toString().padStart(2, '0')}</span>
            <span class="test-title-text">${subject.name} Assessment ${i + 1}</span>
            <span class="test-meta-roll">&bull; Q${startQ.toString().padStart(3, '0')} &ndash; Q${endQ.toString().padStart(3, '0')}</span>
            ${statusPill}
          </div>
          <div class="dashed-pill-box">
            &#10022; Focus: ${topicName}
          </div>
          <div class="test-timestamp">
            Batch size: ${endQ - startQ + 1} Questions &bull; 45 Min Timer &bull; Proctored Mode Active
          </div>
        </div>
        <div class="test-item-actions">
          <button class="btn btn-black" onclick="selectAndLaunchBatch(${i})">
            ${isCompleted ? 'Retake Test' : 'Start Test'} &rarr;
          </button>
        </div>
      `;

      grid.appendChild(card);
    }
  }

  window.selectAndLaunchBatch = function (batchIdx) {
    currentBatchIndex = batchIdx;
    openStartTestModal();
  };

  window.openStartTestModal = function () {
    const subject = window.ALL_SUBJECTS[currentSubjectKey];
    document.getElementById('modal-batch-name').textContent = `Begin ${subject.name} Assessment ${currentBatchIndex + 1}`;
    document.getElementById('start-modal').style.display = 'flex';
  };

  window.closeStartModal = function () {
    document.getElementById('start-modal').style.display = 'none';
  };

  window.confirmLaunchTest = function () {
    closeStartModal();
    const enableCamera = document.getElementById('check-camera').checked;
    const enableFullscreen = document.getElementById('check-fullscreen').checked;

    if (enableFullscreen) {
      try {
        if (!document.fullscreenElement) {
          document.documentElement.requestFullscreen().catch(() => {});
        }
      } catch (e) {}
    }

    startTest(currentBatchIndex, enableCamera);
  };

  // --------------------------------------------------------------------------
  // TEST LAUNCH & NAVIGATION
  // --------------------------------------------------------------------------
  window.startTest = function(batchIdx, enableCamera) {
    currentBatchIndex = batchIdx;
    const subject = window.ALL_SUBJECTS[currentSubjectKey];
    const startIndex = batchIdx * BATCH_SIZE;
    currentTestQuestions = subject.questions.slice(startIndex, startIndex + BATCH_SIZE);

    userAnswers = {};
    reviewFlags = {};
    visitedQuestions = new Set();
    currentQuestionIndex = 0;
    violationCount = 0;
    lastViolationTime = 0;
    testStartTime = Date.now();
    if (violationAutoSubmitTimer) {
      clearTimeout(violationAutoSubmitTimer);
      violationAutoSubmitTimer = null;
    }
    remainingSeconds = DEFAULT_DURATION_SECONDS;
    isTestActive = true;

    hideAllViews();
    testView.style.display = 'block';
    testHeaderStatus.style.display = 'flex';
    const mainNav = document.getElementById('main-nav-links');
    if (mainNav) mainNav.style.display = 'none';

    violationCountEl.textContent = '0';

    startTimer();

    if (enableCamera) {
      initCameraStream();
    } else {
      showCameraFallback();
    }

    renderPalette();
    loadQuestion(0);
  };

  function startTimer() {
    clearInterval(timerInterval);
    updateTimerDisplay();
    timerInterval = setInterval(() => {
      remainingSeconds--;
      updateTimerDisplay();
      if (remainingSeconds <= 0) {
        clearInterval(timerInterval);
        alert('Time is up! Your proctored test is being submitted automatically.');
        executeSubmitTest();
      }
    }, 1000);
  }

  function updateTimerDisplay() {
    const mins = Math.floor(remainingSeconds / 60);
    const secs = remainingSeconds % 60;
    timerDisplay.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  }

  function renderPalette() {
    paletteGrid.innerHTML = '';
    for (let i = 0; i < currentTestQuestions.length; i++) {
      const btn = document.createElement('button');
      btn.className = 'palette-btn';
      btn.id = `palette-btn-${i}`;
      btn.textContent = i + 1;
      btn.onclick = () => loadQuestion(i);
      paletteGrid.appendChild(btn);
    }
    updatePaletteStatus();
  }

  function updatePaletteStatus() {
    let answeredCount = 0;
    for (let i = 0; i < currentTestQuestions.length; i++) {
      const btn = document.getElementById(`palette-btn-${i}`);
      if (!btn) continue;

      btn.className = 'palette-btn';

      if (i === currentQuestionIndex) {
        btn.classList.add('active-q');
      }

      if (reviewFlags[i]) {
        btn.classList.add('flagged');
      } else if (userAnswers[i] !== undefined) {
        btn.classList.add('answered');
        answeredCount++;
      } else if (visitedQuestions.has(i)) {
        btn.classList.add('visited-unanswered');
      }
    }

    paletteSummary.textContent = `${answeredCount} / ${currentTestQuestions.length}`;
  }

  function loadQuestion(index) {
    if (index < 0 || index >= currentTestQuestions.length) return;
    currentQuestionIndex = index;
    visitedQuestions.add(index);

    const q = currentTestQuestions[index];
    const actualQNumber = (currentBatchIndex * BATCH_SIZE) + index + 1;

    currentQCode.textContent = `Q-${actualQNumber.toString().padStart(3, '0')}`;
    currentQPill.textContent = `Question ${index + 1} of ${currentTestQuestions.length}`;
    currentQModule.textContent = q.module || 'Course Module';

    questionText.textContent = q.question;

    optionsList.innerHTML = '';
    const letters = ['A', 'B', 'C', 'D'];

    q.options.forEach((optText, optIdx) => {
      const isSelected = userAnswers[index] === optIdx;
      const box = document.createElement('div');
      box.className = `option-box ${isSelected ? 'selected' : ''}`;
      box.onclick = () => selectOption(optIdx);

      box.innerHTML = `
        <div class="option-letter">${letters[optIdx]}</div>
        <div class="option-text-content">${optText}</div>
      `;
      optionsList.appendChild(box);
    });

    if (reviewFlags[index]) {
      flagBtn.classList.add('btn-yellow');
      flagBtnText.textContent = '★ Flagged for Review';
    } else {
      flagBtn.classList.remove('btn-yellow');
      flagBtnText.textContent = '⚐ Mark for Review';
    }

    updatePaletteStatus();
  }

  function selectOption(optIdx) {
    userAnswers[currentQuestionIndex] = optIdx;
    loadQuestion(currentQuestionIndex);
  }

  window.navigateQuestion = function (delta) {
    const nextIdx = currentQuestionIndex + delta;
    if (nextIdx >= 0 && nextIdx < currentTestQuestions.length) {
      loadQuestion(nextIdx);
    }
  };

  window.clearCurrentSelection = function () {
    delete userAnswers[currentQuestionIndex];
    loadQuestion(currentQuestionIndex);
  };

  window.toggleReviewFlag = function () {
    if (reviewFlags[currentQuestionIndex]) {
      delete reviewFlags[currentQuestionIndex];
    } else {
      reviewFlags[currentQuestionIndex] = true;
    }
    loadQuestion(currentQuestionIndex);
  };

  // Keyboard navigation
  window.addEventListener('keydown', (e) => {
    if (!isTestActive) return;
    if (e.key === 'ArrowRight') navigateQuestion(1);
    if (e.key === 'ArrowLeft') navigateQuestion(-1);
    if (['1', '2', '3', '4'].includes(e.key)) {
      selectOption(parseInt(e.key, 10) - 1);
    }
  });

  // --------------------------------------------------------------------------
  // PROCTORING ENGINE (CAMERA & SCREEN DETECTION)
  // --------------------------------------------------------------------------
  window.initCameraStream = function () {
    const video = document.getElementById('webcam-video');
    const fallback = document.getElementById('cam-fallback');
    const statusLabel = document.getElementById('cam-status-label');

    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({
        video: { width: { ideal: 640 }, height: { ideal: 480 }, facingMode: 'user' }
      })
      .then((stream) => {
        mediaStream = stream;
        video.srcObject = stream;
        video.style.display = 'block';
        video.style.position = 'absolute';
        video.style.top = '0';
        video.style.left = '0';
        video.style.width = '100%';
        video.style.height = '100%';
        video.style.objectFit = 'cover';
        video.style.transform = 'scaleX(-1)';
        video.style.zIndex = '1';
        video.onloadedmetadata = () => {
          video.play().catch(() => {});
        };
        fallback.style.display = 'none';
        statusLabel.textContent = 'VERIFIED';
      })
      .catch((err) => {
        showCameraFallback();
      });
    } else {
      showCameraFallback();
    }
  };

  function showCameraFallback() {
    const video = document.getElementById('webcam-video');
    const fallback = document.getElementById('cam-fallback');
    const statusLabel = document.getElementById('cam-status-label');
    video.style.display = 'none';
    fallback.style.display = 'flex';
    statusLabel.textContent = 'SIMULATED';
  }

  function stopCameraStream() {
    if (mediaStream) {
      mediaStream.getTracks().forEach(track => track.stop());
      mediaStream = null;
    }
  }

  function setupSecurityListeners() {
    document.addEventListener('visibilitychange', () => {
      if (isTestActive && document.hidden) {
        handleProctorViolation('Tab switched or minimized');
      }
    });

    window.addEventListener('blur', () => {
      if (isTestActive) {
        handleProctorViolation('Window focus lost');
      }
    });

    document.addEventListener('contextmenu', (e) => {
      if (isTestActive) e.preventDefault();
    });

    document.addEventListener('copy', (e) => {
      if (isTestActive) e.preventDefault();
    });
  }

  function handleProctorViolation(reason) {
    if (!isTestActive) return;

    // Grace period for first 4 seconds after test launch (e.g. camera permission dialogs)
    if (Date.now() - testStartTime < 4000) return;

    // Prevent duplicate triggers while the violation modal is already displayed
    const modal = document.getElementById('violation-modal');
    if (modal && modal.style.display === 'flex') return;

    // Debounce rapid successive events (e.g. visibilitychange + blur triggering on same action)
    const now = Date.now();
    if (now - lastViolationTime < 2500) return;
    lastViolationTime = now;

    violationCount++;
    violationCountEl.textContent = violationCount;

    const modalCountEl = document.getElementById('modal-violation-count');
    const modalMsgEl = document.getElementById('violation-modal-msg');
    const dismissBtn = document.getElementById('violation-dismiss-btn');

    if (violationCount >= 3) {
      if (modalCountEl) modalCountEl.textContent = '3';
      if (modalMsgEl) {
        modalMsgEl.textContent =
          `Integrity threshold breached (3 of 3 strikes): ${reason}. Your assessment has been automatically locked and submitted.`;
      }
      if (dismissBtn) {
        dismissBtn.textContent = 'Submit Assessment Now';
        dismissBtn.onclick = function () {
          dismissViolationModal();
          executeSubmitTest();
        };
      }
      modal.style.display = 'flex';

      // Auto-submit test after 3 seconds on final strike
      if (violationAutoSubmitTimer) clearTimeout(violationAutoSubmitTimer);
      violationAutoSubmitTimer = setTimeout(() => {
        if (isTestActive) {
          dismissViolationModal();
          executeSubmitTest();
        }
      }, 3000);
      return;
    }

    if (modalCountEl) modalCountEl.textContent = violationCount;
    if (modalMsgEl) {
      const remainingStrikes = 3 - violationCount;
      modalMsgEl.textContent =
        `Security check triggered: ${reason}. Please keep this assessment window focused. (${remainingStrikes} warning strike${remainingStrikes === 1 ? '' : 's'} remaining).`;
    }
    if (dismissBtn) {
      dismissBtn.textContent = 'I Understand \u2014 Return to Assessment';
      dismissBtn.onclick = dismissViolationModal;
    }
    modal.style.display = 'flex';
  }

  window.dismissViolationModal = function () {
    if (violationAutoSubmitTimer) {
      clearTimeout(violationAutoSubmitTimer);
      violationAutoSubmitTimer = null;
    }
    const modal = document.getElementById('violation-modal');
    if (modal) modal.style.display = 'none';
  };

  // --------------------------------------------------------------------------
  // SUBMISSION & RESULTS
  // --------------------------------------------------------------------------
  window.confirmSubmitTest = function () {
    const answeredCount = Object.keys(userAnswers).length;
    document.getElementById('submit-summary-text').textContent =
      `You have answered ${answeredCount} of ${currentTestQuestions.length} questions. Submit for final scoring?`;
    document.getElementById('submit-modal').style.display = 'flex';
  };

  window.closeSubmitModal = function () {
    document.getElementById('submit-modal').style.display = 'none';
  };

  window.executeSubmitTest = function () {
    if (violationAutoSubmitTimer) {
      clearTimeout(violationAutoSubmitTimer);
      violationAutoSubmitTimer = null;
    }
    closeSubmitModal();
    clearInterval(timerInterval);
    isTestActive = false;
    stopCameraStream();

    let correctCount = 0;
    let incorrectCount = 0;
    let skippedCount = 0;

    currentTestQuestions.forEach((q, idx) => {
      const userChoice = userAnswers[idx];
      if (userChoice === undefined) {
        skippedCount++;
      } else if (userChoice === q.correct) {
        correctCount++;
      } else {
        incorrectCount++;
      }
    });

    const total = currentTestQuestions.length;
    const percentage = Math.round((correctCount / total) * 100);
    const xpGained = correctCount * 4;

    const progress = getProgressData();
    if (!progress[currentSubjectKey]) {
      progress[currentSubjectKey] = { completedBatches: {}, totalXp: 0 };
    }
    progress[currentSubjectKey].completedBatches[currentBatchIndex] = {
      score: correctCount,
      total: total,
      userAnswers: userAnswers,
      violations: violationCount,
      timestamp: Date.now()
    };
    progress[currentSubjectKey].totalXp = (progress[currentSubjectKey].totalXp || 0) + xpGained;
    saveProgressData(progress);

    showResultsView(correctCount, incorrectCount, skippedCount, percentage, xpGained);
  };

  function showResultsView(correct, incorrect, skipped, pct, xp) {
    hideAllViews();
    resultView.style.display = 'block';
    testHeaderStatus.style.display = 'none';
    const mainNav = document.getElementById('main-nav-links');
    if (mainNav) mainNav.style.display = 'flex';

    document.getElementById('score-percentage').textContent = `${pct}%`;
    document.getElementById('score-fraction').textContent = `${correct} / ${currentTestQuestions.length} Correct`;
    document.getElementById('res-correct').textContent = correct;
    document.getElementById('res-incorrect').textContent = incorrect;
    document.getElementById('res-skipped').textContent = skipped;
    document.getElementById('res-xp').textContent = `+${xp}`;
    document.getElementById('res-violations').textContent = violationCount;

    const verdict = document.getElementById('result-verdict');
    const msg = document.getElementById('result-message');

    if (pct >= 80) {
      verdict.textContent = 'Assessment Mastered!';
      msg.textContent = 'Outstanding grasp of the concepts. Keep up the high standard!';
    } else if (pct >= 50) {
      verdict.textContent = 'Assessment Cleared — Solid Performance';
      msg.textContent = 'Good foundational understanding. Review question-by-question analysis below.';
    } else {
      verdict.textContent = 'Further Study Recommended';
      msg.textContent = 'Review incorrect answers below and revisit course notes to improve.';
    }

    renderReviewList('all');
  }

  window.filterReview = function (type) {
    isReviewFilter = type;
    document.querySelectorAll('.review-header-flex .filter-pill').forEach(tab => {
      tab.classList.toggle('active', tab.getAttribute('data-filter') === type);
    });
    renderReviewList(type);
  };

  function renderReviewList(filter) {
    const container = document.getElementById('review-list');
    container.innerHTML = '';
    const letters = ['A', 'B', 'C', 'D'];

    currentTestQuestions.forEach((q, idx) => {
      const userChoice = userAnswers[idx];
      const isCorrect = userChoice === q.correct;
      const isSkipped = userChoice === undefined;
      const isFlagged = !!reviewFlags[idx];

      if (filter === 'correct' && !isCorrect) return;
      if (filter === 'incorrect' && (isCorrect || isSkipped)) return;
      if (filter === 'marked' && !isFlagged) return;

      const card = document.createElement('div');
      card.className = 'review-item-box';

      let tagPill = '<span class="tag-pill neutral-pill">SKIPPED</span>';
      if (!isSkipped) {
        tagPill = isCorrect
          ? '<span class="tag-pill yellow-pill" style="background: #dcfce7; color: #166534;">CORRECT (+4 XP)</span>'
          : '<span class="tag-pill neutral-pill" style="background: #fee2e2; color: #991b1b;">INCORRECT (0 XP)</span>';
      }

      let optionsHtml = '';
      q.options.forEach((optText, optIdx) => {
        let optClass = 'review-opt-item';
        let marker = '';

        if (optIdx === q.correct) {
          optClass += ' is-correct';
          marker = ' &check; (Correct Answer)';
        }
        if (optIdx === userChoice && !isCorrect) {
          optClass += ' is-incorrect';
          marker = ' &cross; (Your Choice)';
        }

        optionsHtml += `
          <div class="${optClass}">
            <strong>${letters[optIdx]}.</strong> ${optText} ${marker}
          </div>
        `;
      });

      card.innerHTML = `
        <div class="review-item-header">
          <div class="tags-cluster">
            <span class="tag-pill yellow-pill">Q${idx + 1}</span>
            <span class="mono-bold">${q.module}</span>
          </div>
          ${tagPill}
        </div>
        <div class="review-q-title">${q.question}</div>
        <div class="review-options-group">
          ${optionsHtml}
        </div>
        <div class="review-explanation-callout">
          <strong>Conceptual Analysis:</strong> ${q.explanation}
        </div>
      `;

      container.appendChild(card);
    });
  }

  window.startNextUnseenBatch = function () {
    const subject = window.ALL_SUBJECTS[currentSubjectKey];
    const progress = getProgressData();
    const subProgress = progress[currentSubjectKey] || { completedBatches: {} };
    const totalBatches = Math.ceil(subject.total / BATCH_SIZE);

    let nextIdx = (currentBatchIndex + 1) % totalBatches;
    
    for (let i = 0; i < totalBatches; i++) {
      const candidate = (currentBatchIndex + 1 + i) % totalBatches;
      if (!subProgress.completedBatches[candidate]) {
        nextIdx = candidate;
        break;
      }
    }

    startTest(nextIdx, true);
  };

  window.showDashboard = function () {
    selectSubject(currentSubjectKey);
  };

  // Direct Link Hook
  window.addEventListener('DOMContentLoaded', () => {
    const params = new URLSearchParams(window.location.search);
    if (params.has('signin')) {
      showSignInScreen();
      return;
    }
    if (params.has('subject')) {
      const s = params.get('subject');
      if (window.ALL_SUBJECTS && window.ALL_SUBJECTS[s]) {
        selectSubject(s);
      }
    }
  });

})();
