# IMPORTANT: Save this file as 'app.py' (NOT .html)
# Run from terminal using: python app.py

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="SHIELD-E-MAX Product Matrix")

MAIN_HTML_OUTPUT = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SHIELD-E-MAX | Next-Gen E20 Fuel Phase Stabilization Matrix</title>
    
    <!-- CDNs -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    <script src="https://unpkg.com/lucide@latest"></script>

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: { navy: '#0F172A', emerald: '#10B981', teal: '#0EA5E9' },
                    boxShadow: { 'glass': '0 8px 32px 0 rgba(31, 38, 135, 0.07)' }
                }
            }
        }
    </script>
    
    <style>
        .glass-card { background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(12.5px); -webkit-backdrop-filter: blur(12.5px); border: 1px solid rgba(255, 255, 255, 0.18); border-radius: 20px; }
        .glass-nav { background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); }
        @keyframes pulse-emerald { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.7; transform: scale(1.05); } }
        .emerald-pulse { animation: pulse-emerald 2s cubic-bezier(0.4, 0, 0.6, 1) infinite; }
        ::-webkit-scrollbar { width: 8px; background: #F8FAFC; }
        ::-webkit-scrollbar-thumb { background: #CBD5E1; border-radius: 4px; }
        .sim-canvas { outline: none; width: 100%; height: 100%; }
        html { scroll-behavior: smooth; }
    </style>
</head>
<body class="bg-[#F8FAFC] text-slate-900 antialiased font-sans flex flex-col min-h-screen">

    <!-- NAVIGATION HEADER -->
    <header class="glass-nav sticky top-0 z-50 w-full border-b border-gray-200 shadow-sm">
        <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex items-center justify-between">
            <div class="flex items-center gap-2">
                <i data-lucide="shield-check" class="w-8 h-8 text-navy"></i>
                <span class="text-2xl md:text-3xl font-black text-navy tracking-tighter">SHIELD-<span class="text-emerald">E</span>-MAX</span>
            </div>
            
            <div class="hidden lg:flex items-center gap-6 text-sm font-bold text-gray-600">
                <a href="#about" class="hover:text-emerald transition-colors">About</a>
                <a href="#simulations" class="hover:text-emerald transition-colors">Interactive Sims</a>
                <a href="#calculator" class="hover:text-emerald transition-colors">Economics</a>
            </div>

            <div class="flex items-center gap-3">
                <div class="hidden md:flex items-center gap-2 border border-gray-200 px-3 py-1.5 rounded-full bg-white shadow-sm">
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald emerald-pulse"></span>
                    <span class="text-xs font-bold text-gray-600">SYSTEM: ONLINE</span>
                </div>
                <!-- DIRECTS TO NEW PAGE -->
                <a href="/buy" target="_blank" class="bg-emerald text-white px-5 py-2.5 rounded-lg text-sm font-bold shadow-md hover:bg-emerald/90 hover:shadow-lg transition-all flex items-center gap-2">
                    <i data-lucide="shopping-cart" class="w-4 h-4"></i> Buy Now
                </a>
            </div>
        </nav>
    </header>

    <main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full py-12 space-y-24">

        <!-- HERO SECTION -->
        <section id="overview" class="grid grid-cols-1 lg:grid-cols-2 items-center gap-12 pt-8">
            <div class="space-y-6">
                <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-teal/10 text-teal font-bold text-sm">
                    <i data-lucide="zap" class="w-4 h-4"></i> Disrupting E20 Stability
                </div>
                <h1 class="text-5xl md:text-7xl font-black tracking-tighter text-navy leading-[1.05]">
                    Next-Gen E20 Fuel Additive & <span class="text-transparent bg-clip-text bg-gradient-to-r from-teal to-emerald">Phase Stabilization</span> Matrix
                </h1>
                <p class="text-xl text-gray-700 font-medium max-w-2xl">
                    SHIELD-E-MAX chemically bridges high-ethanol gasoline blends. Formulated with sterically hindered alkyl-amines for complete <span class="font-bold text-emerald">20% ethanol blend protection</span>, dynamic pH buffering, and zero-soot combustion.
                </p>
                <div class="flex flex-col sm:flex-row items-center gap-4 pt-4">
                    <a href="#simulations" class="w-full sm:w-auto flex items-center justify-center gap-2 bg-navy text-white px-8 py-4 rounded-xl font-bold text-lg shadow-lg hover:shadow-xl hover:bg-navy/90 transition-all">
                        <i data-lucide="play" class="w-5 h-5"></i> Run Simulations
                    </a>
                    <a href="#calculator" class="w-full sm:w-auto flex items-center justify-center gap-2 bg-white text-navy border-2 border-gray-200 px-8 py-4 rounded-xl font-bold text-lg hover:border-navy transition-all shadow-sm">
                        <i data-lucide="calculator" class="w-5 h-5"></i> Cost Calculator
                    </a>
                </div>
            </div>
            <div class="glass-card p-8 shadow-glass border-t-4 border-t-teal flex flex-col justify-center relative overflow-hidden">
                <div class="absolute -right-10 -top-10 text-[200px] text-gray-50 opacity-50 pointer-events-none">
                    <i data-lucide="flask-conical"></i>
                </div>
                <h3 class="text-2xl font-black text-navy flex items-center gap-2 mb-6 relative z-10"><i data-lucide="activity" class="text-emerald"></i> The 70:20:10 Disruption</h3>
                <div class="grid grid-cols-1 gap-4 relative z-10">
                    <div class="bg-gray-50 p-5 rounded-2xl border border-gray-100 flex items-start gap-4">
                        <div class="bg-white p-3 rounded-xl shadow-sm"><i data-lucide="droplet" class="text-blue-500 w-6 h-6"></i></div>
                        <div>
                            <h4 class="font-bold text-navy text-base">70% Amine Buffer (Phase Shield)</h4>
                            <p class="text-sm text-gray-600 font-medium mt-1">Cages water clusters, preventing >90-day phase separation.</p>
                        </div>
                    </div>
                    <div class="bg-gray-50 p-5 rounded-2xl border border-gray-100 flex items-start gap-4">
                        <div class="bg-white p-3 rounded-xl shadow-sm"><i data-lucide="combine" class="text-teal w-6 h-6"></i></div>
                        <div>
                            <h4 class="font-bold text-navy text-base">20% DMC (Co-Solvent Bridge)</h4>
                            <p class="text-sm text-gray-600 font-medium mt-1">Reduces miscibility gap tension for a clean, stable burn.</p>
                        </div>
                    </div>
                    <div class="bg-gray-50 p-5 rounded-2xl border border-gray-100 flex items-start gap-4">
                        <div class="bg-white p-3 rounded-xl shadow-sm"><i data-lucide="flame" class="text-orange-500 w-6 h-6"></i></div>
                        <div>
                            <h4 class="font-bold text-navy text-base">10% DTBP (Kinetic Restorer)</h4>
                            <p class="text-sm text-gray-600 font-medium mt-1">Accelerates flame speed, yielding +4.2% ΔBTE efficiency gain.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ABOUT SECTION -->
        <section id="about" class="space-y-8 bg-white p-10 rounded-[2.5rem] shadow-sm border border-gray-100">
            <div class="text-center max-w-4xl mx-auto space-y-4">
                <span class="text-teal font-bold tracking-widest text-sm uppercase">About The Portal</span>
                <h2 class="text-4xl md:text-5xl font-black text-navy tracking-tight">Bridging India's E20 Mandate</h2>
                <p class="text-lg text-gray-600 font-medium pt-2 leading-relaxed">
                    SHIELD-E-MAX is a comprehensive B2B portal and predictive thermodynamics engine designed for oil marketing companies, fuel terminals, and large fleet operators. As India shifts to a mandatory 20% ethanol blend (E20), 85% of legacy vehicles face severe operational risks including phase separation (water drop-out) and acidic corrosion. Our platform provides the mandated chemical solution, backed by live computational physics, to guarantee hardware protection at a negligible cost of ₹0.12/Liter.
                </p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 pt-6">
                <div class="p-6 bg-[#F8FAFC] rounded-2xl border border-gray-200">
                    <i data-lucide="check-circle-2" class="w-8 h-8 text-emerald mb-4"></i>
                    <h4 class="font-bold text-navy text-lg mb-2">ASTM Validated</h4>
                    <p class="text-sm text-gray-600">Passes ASTM D665/D130 for severe rust and copper corrosion inhibition in harsh environments.</p>
                </div>
                <div class="p-6 bg-[#F8FAFC] rounded-2xl border border-gray-200">
                    <i data-lucide="trending-up" class="w-8 h-8 text-teal mb-4"></i>
                    <h4 class="font-bold text-navy text-lg mb-2">Cost-Optimized Dosing</h4>
                    <p class="text-sm text-gray-600">Algorithmic dosing targets a highly potent 1,200 PPM treat rate, balancing minimal OPEX with maximum ROI.</p>
                </div>
                <div class="p-6 bg-[#F8FAFC] rounded-2xl border border-gray-200">
                    <i data-lucide="factory" class="w-8 h-8 text-blue-500 mb-4"></i>
                    <h4 class="font-bold text-navy text-lg mb-2">Industrial Scalability</h4>
                    <p class="text-sm text-gray-600">Direct integration capabilities for in-line terminal doping and large-scale depot batch mixing.</p>
                </div>
            </div>
        </section>

        <!-- INTERACTIVE SIMULATIONS -->
        <section id="simulations" class="space-y-8">
            <div class="text-center max-w-3xl mx-auto space-y-4">
                <i data-lucide="monitor-play" class="w-12 h-12 text-navy mx-auto mb-2"></i>
                <h2 class="text-4xl md:text-5xl font-black text-navy tracking-tight">Interactive Digital Twins</h2>
                <p class="text-lg text-gray-700 font-medium">Explore the physical chemistry of SHIELD-E-MAX through our WebGL powered physics engines.</p>
            </div>

            <!-- Dashboard Controls -->
            <div class="glass-card shadow-glass p-6 md:p-8 flex flex-col lg:flex-row gap-8 items-center justify-between">
                <div class="flex items-center gap-2 bg-gray-100 p-1.5 rounded-2xl border border-gray-200 flex-wrap">
                    <button onclick="switchSim('tank')" id="btn-tank" class="px-5 py-2.5 rounded-xl font-bold text-sm bg-white text-navy shadow-sm transition-all flex items-center gap-2"><i data-lucide="database"></i> In-Tank Phase</button>
                    <button onclick="switchSim('combustion')" id="btn-combustion" class="px-5 py-2.5 rounded-xl font-bold text-sm text-gray-500 hover:text-navy transition-all flex items-center gap-2"><i data-lucide="flame-kindling"></i> Engine Kinetics</button>
                    <button onclick="switchSim('molecule')" id="btn-molecule" class="px-5 py-2.5 rounded-xl font-bold text-sm text-gray-500 hover:text-navy transition-all flex items-center gap-2"><i data-lucide="atom"></i> C14 Molecule</button>
                </div>
                
                <div class="flex items-center gap-4 w-full lg:w-auto">
                    <span class="text-sm font-bold text-gray-500 uppercase tracking-wider whitespace-nowrap">Fuel State:</span>
                    <select id="sim-state-select" class="w-full lg:w-64 p-3 bg-white border-2 border-gray-200 rounded-xl font-bold text-navy outline-none focus:border-teal" onchange="updateSimulationState()">
                        <option value="untreated">Raw E20 (Untreated & Unstable)</option>
                        <option value="treated" selected>E20 + SHIELD-E-MAX (Stabilized)</option>
                    </select>
                </div>
            </div>

            <!-- Simulation Canvases -->
            <div class="h-[500px] md:h-[600px] rounded-[2rem] overflow-hidden relative shadow-2xl bg-navy border-4 border-gray-800">
                
                <!-- Tank View -->
                <div id="view-tank" class="absolute inset-0 transition-opacity duration-500 opacity-100 z-10">
                    <div class="absolute top-6 left-6 z-20 bg-white/90 backdrop-blur px-4 py-3 rounded-xl shadow-lg border border-white">
                        <h3 class="font-bold text-navy">Storage Tank Physics</h3>
                        <p id="tank-desc" class="text-xs font-semibold text-emerald">Stable Micro-Emulsion. Water encapsulated.</p>
                    </div>
                    <canvas id="canvas-tank" class="sim-canvas"></canvas>
                </div>

                <!-- Combustion View -->
                <div id="view-combustion" class="absolute inset-0 transition-opacity duration-500 opacity-0 z-0">
                    <div class="absolute top-6 left-6 z-20 bg-white/90 backdrop-blur px-4 py-3 rounded-xl shadow-lg border border-white">
                        <h3 class="font-bold text-navy">Cylinder Combustion</h3>
                        <p id="comb-desc" class="text-xs font-semibold text-emerald">Optimized flame speed. +4.2% BTE.</p>
                    </div>
                    <canvas id="canvas-combustion" class="sim-canvas"></canvas>
                </div>

                <!-- Molecule View -->
                <div id="view-molecule" class="absolute inset-0 transition-opacity duration-500 opacity-0 z-0 bg-[#0B1120]">
                    <div class="absolute top-6 left-6 z-20 bg-white/10 backdrop-blur px-4 py-3 rounded-xl shadow-lg border border-white/20">
                        <h3 class="font-bold text-white">Tri-tetradecylamine Buffer</h3>
                        <p class="text-xs font-semibold text-teal-400">Drag to rotate 360°. Scroll to zoom.</p>
                    </div>
                    <canvas id="canvas-molecule" class="sim-canvas"></canvas>
                </div>

            </div>
        </section>

        <!-- CALCULATOR SECTION -->
        <section id="calculator" class="space-y-12">
            <div class="text-center max-w-3xl mx-auto">
                <i data-lucide="calculator" class="w-16 h-16 text-teal mx-auto mb-4 bg-white p-3 rounded-2xl shadow-sm border border-gray-100"></i>
                <h2 class="text-4xl md:text-5xl font-black text-navy tracking-tight">Fuel Batch & Cost Calculator</h2>
                <p class="text-lg text-gray-700 font-medium pt-3">
                    Calculate precise additive requirements and projected financial ROI based on Python-validated manufacturing simulations.
                </p>
            </div>
            
            <div class="glass-card shadow-glass p-8 md:p-10 grid grid-cols-1 md:grid-cols-12 gap-10">
                <div class="md:col-span-5 space-y-6">
                    <h3 class="text-2xl font-bold text-navy flex items-center gap-2"><i data-lucide="sliders-horizontal" class="w-6 h-6 text-emerald"></i> Input Parameters</h3>
                    
                    <div class="space-y-1.5">
                        <label class="font-bold text-gray-700 text-sm">Fuel Batch Volume (Liters)</label>
                        <div class="relative">
                            <i data-lucide="container" class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400"></i>
                            <input type="number" id="input-volume" value="10000" class="w-full bg-white border-2 border-gray-200 pl-12 pr-4 py-3 rounded-xl font-bold text-lg text-navy focus:border-teal transition outline-none shadow-inner">
                        </div>
                    </div>
                    <div class="space-y-1.5">
                        <label class="font-bold text-gray-700 text-sm">Target Ethanol Blend (%)</label>
                        <div class="flex items-center gap-2 bg-white border-2 border-gray-200 rounded-xl p-2 shadow-inner">
                            <input type="range" id="input-blend" min="5" max="30" value="20" class="flex-1 accent-teal" oninput="document.getElementById('blend-val-display').innerText = this.value + '%'">
                            <span id="blend-val-display" class="font-black text-navy w-12 text-center">20%</span>
                        </div>
                    </div>
                    <div class="space-y-1.5">
                        <label class="font-bold text-gray-700 text-sm">Treat Rate Ratio (Optimal 1:150)</label>
                        <div class="relative">
                            <i data-lucide="percent" class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400"></i>
                            <input type="number" id="input-rate" value="150" class="w-full bg-white border-2 border-gray-200 pl-12 pr-4 py-3 rounded-xl font-bold text-lg text-navy focus:border-teal transition outline-none shadow-inner">
                        </div>
                    </div>
                    
                    <button id="calculate-btn" class="w-full bg-navy text-white py-4 rounded-xl font-bold text-xl shadow-lg hover:shadow-xl hover:bg-navy/90 transition-all flex items-center justify-center gap-2 mt-4">
                        <i data-lucide="bar-chart-3" class="w-6 h-6"></i> Run Economic Analysis
                    </button>
                </div>
                
                <div class="md:col-span-7 bg-white border border-gray-200 rounded-3xl p-8 space-y-8 shadow-sm flex flex-col justify-between">
                    <div class="flex items-center justify-between border-b pb-4">
                        <h3 class="text-2xl font-bold text-navy flex items-center gap-2"><i data-lucide="target" class="w-6 h-6 text-teal"></i> Projection Results</h3>
                        <span class="px-3 py-1 bg-gray-100 rounded-full text-xs font-bold text-gray-500 uppercase" id="calc-status">Ready</span>
                    </div>
                    
                    <div class="grid grid-cols-2 gap-4">
                        <div class="bg-gray-50 p-6 rounded-2xl border border-gray-100 flex flex-col justify-center transition-all hover:border-teal/30 hover:shadow-md">
                            <span class="text-xs font-bold text-gray-500 uppercase tracking-widest">Required Dose</span>
                            <div class="flex items-baseline gap-2 mt-2">
                                <span class="text-4xl font-black text-navy" id="output-dose">13.3</span>
                                <span class="font-bold text-gray-500">Liters</span>
                            </div>
                        </div>
                        <div class="bg-gray-50 p-6 rounded-2xl border border-gray-100 flex flex-col justify-center transition-all hover:border-emerald/30 hover:shadow-md">
                            <span class="text-xs font-bold text-gray-500 uppercase tracking-widest">Est. Batch Cost</span>
                            <div class="flex items-baseline gap-2 mt-2">
                                <span class="text-xl font-bold text-gray-400">₹</span>
                                <span class="text-4xl font-black text-navy" id="output-cost">4,200</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="bg-emerald/5 border-2 border-emerald/20 p-6 rounded-2xl flex items-center justify-between">
                         <div>
                             <span class="text-xs font-bold text-emerald uppercase tracking-widest">Incremental Consumer Cost</span>
                             <div class="flex items-baseline gap-2 mt-1">
                                 <span class="text-5xl font-black text-emerald" id="output-per-liter">₹0.12</span>
                                 <span class="font-bold text-emerald/70 text-lg">/ Liter</span>
                             </div>
                         </div>
                         <div class="hidden sm:block text-right">
                              <span class="text-xs font-bold text-gray-500 uppercase">Efficiency Savings</span>
                              <span class="block text-2xl font-black text-navy mt-1" id="output-savings">₹40,320</span>
                         </div>
                    </div>
                </div>
            </div>
        </section>

    </main>

    <!-- FOOTER -->
    <footer class="bg-navy text-white/70 py-12 border-t border-gray-800 mt-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full text-center space-y-4">
            <div class="flex items-center gap-2 justify-center">
                <i data-lucide="shield-check" class="w-6 h-6 text-white"></i>
                <span class="text-xl font-black tracking-tighter text-white">SHIELD-<span class="text-emerald">E</span>-MAX</span>
            </div>
            <p class="text-sm font-semibold max-w-lg mx-auto">Proprietary Sterically Hindered Amine Formulation. Mandate-Ready Infrastructure.</p>
            <p class="text-xs text-gray-500">&copy; 2026 Shield-E-Max Thermodynamics Group. All Rights Reserved.</p>
        </div>
    </footer>

    <script>
        lucide.createIcons();

        // --- CALCULATOR LOGIC ---
        document.getElementById('calculate-btn').addEventListener('click', function() {
            const btn = this;
            const orig = btn.innerHTML;
            btn.innerHTML = '<i data-lucide="loader-2" class="w-6 h-6 animate-spin"></i> Processing...';
            lucide.createIcons();
            
            setTimeout(() => {
                const vol = parseFloat(document.getElementById('input-volume').value) || 0;
                const blend = parseFloat(document.getElementById('input-blend').value) || 0;
                const rateRatio = parseFloat(document.getElementById('input-rate').value) || 1;

                if (vol > 0 && blend > 0 && rateRatio > 0) {
                    const ethanolVol = vol * (blend / 100.0);
                    const additiveVol = ethanolVol / rateRatio;
                    const costPerLAdditive = 315.0; // ₹
                    const batchCost = additiveVol * costPerLAdditive;
                    const opExPer10k = 150;
                    const totalCostBatch = batchCost + (vol / 10000) * opExPer10k;
                    const costPerLiter = totalCostBatch / vol;
                    
                    const bteBoost = Math.min(5.8, (150.0 / rateRatio) * 4.2);
                    const fuelPricePerL = 96.50;
                    const efficiencySavings = vol * fuelPricePerL * (bteBoost / 100.0);

                    document.getElementById('output-dose').innerText = additiveVol.toFixed(1);
                    document.getElementById('output-cost').innerText = Math.round(batchCost).toLocaleString();
                    document.getElementById('output-per-liter').innerText = '₹' + costPerLiter.toFixed(2);
                    document.getElementById('output-savings').innerText = '₹' + Math.round(efficiencySavings).toLocaleString();
                    
                    const status = document.getElementById('calc-status');
                    status.innerText = 'Computed successfully';
                    status.className = 'px-3 py-1 bg-emerald/10 text-emerald rounded-full text-xs font-bold uppercase';
                }
                btn.innerHTML = orig;
                lucide.createIcons();
            }, 400);
        });

        // --- 3D SIMULATION ENGINE ---
        let activeTab = 'tank';
        let isTreated = true;

        function switchSim(tab) {
            activeTab = tab;
            ['tank', 'combustion', 'molecule'].forEach(t => {
                document.getElementById('view-' + t).classList.toggle('opacity-0', t !== tab);
                document.getElementById('view-' + t).classList.toggle('z-10', t === tab);
                document.getElementById('view-' + t).classList.toggle('z-0', t !== tab);
                
                const btn = document.getElementById('btn-' + t);
                if(t === tab) {
                    btn.classList.add('bg-white', 'text-navy', 'shadow-sm');
                    btn.classList.remove('text-gray-500');
                } else {
                    btn.classList.remove('bg-white', 'text-navy', 'shadow-sm');
                    btn.classList.add('text-gray-500');
                }
            });
        }

        function updateSimulationState() {
            isTreated = document.getElementById('sim-state-select').value === 'treated';
            
            // Update UI text descriptions
            const tDesc = document.getElementById('tank-desc');
            const cDesc = document.getElementById('comb-desc');
            
            if(isTreated) {
                tDesc.innerText = "Stable Micro-Emulsion. Water encapsulated.";
                tDesc.className = "text-xs font-semibold text-emerald";
                cDesc.innerText = "Optimized flame speed. +4.2% BTE.";
                cDesc.className = "text-xs font-semibold text-emerald";
            } else {
                tDesc.innerText = "Phase Separation. Free water sinking.";
                tDesc.className = "text-xs font-semibold text-red-500";
                cDesc.innerText = "Ignition Delay. Slow, sooty burn.";
                cDesc.className = "text-xs font-semibold text-orange-500";
            }
        }

        function setupScene(canvasId) {
            const canvas = document.getElementById(canvasId);
            const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
            const camera = new THREE.PerspectiveCamera(45, canvas.clientWidth / canvas.clientHeight, 0.1, 1000);
            const scene = new THREE.Scene();
            const controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;

            function resize() {
                if(canvas.clientWidth > 0) {
                    camera.aspect = canvas.clientWidth / canvas.clientHeight;
                    camera.updateProjectionMatrix();
                    renderer.setSize(canvas.clientWidth, canvas.clientHeight, false);
                }
            }
            window.addEventListener('resize', resize);
            setTimeout(resize, 100);
            
            return { scene, camera, renderer, controls };
        }

        // 1. Tank Physics (Phase Separation vs Stable Emulsion)
        const tankSys = setupScene('canvas-tank');
        tankSys.camera.position.set(0, 5, 30);
        tankSys.controls.autoRotate = true;
        
        tankSys.scene.add(new THREE.Mesh(
            new THREE.CylinderGeometry(8, 8, 16, 32, 1, true),
            new THREE.MeshPhysicalMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.1, side: THREE.DoubleSide })
        ));
        tankSys.scene.add(new THREE.LineSegments(
            new THREE.EdgesGeometry(new THREE.CylinderGeometry(8, 8, 16, 16)),
            new THREE.LineBasicMaterial({ color: 0x0ea5e9, transparent: true, opacity: 0.2 })
        ));

        const pCount = 1500;
        const pGeo = new THREE.BufferGeometry();
        const pPos = new Float32Array(pCount * 3);
        const pCol = new Float32Array(pCount * 3);
        const pData = []; 

        const cHydro = new THREE.Color('#14b8a6');
        const cWater = new THREE.Color('#ef4444');
        const cMicelle = new THREE.Color('#10B981'); // Emerald when treated

        for(let i=0; i<pCount; i++) {
            const r = 7.5 * Math.sqrt(Math.random());
            const theta = Math.random() * 2 * Math.PI;
            pPos[i*3] = r * Math.cos(theta);
            pPos[i*3+1] = (Math.random() - 0.5) * 15;
            pPos[i*3+2] = r * Math.sin(theta);
            
            pData.push({ yVel: (Math.random() - 0.5) * 0.05, isWater: Math.random() < 0.15 });
        }
        pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
        pGeo.setAttribute('color', new THREE.BufferAttribute(pCol, 3));

        const spriteCanvas = document.createElement('canvas');
        spriteCanvas.width = 16; spriteCanvas.height = 16;
        const sCtx = spriteCanvas.getContext('2d');
        sCtx.beginPath(); sCtx.arc(8, 8, 8, 0, Math.PI * 2); sCtx.fillStyle = 'white'; sCtx.fill();
        
        const pMat = new THREE.PointsMaterial({ size: 0.5, vertexColors: true, map: new THREE.CanvasTexture(spriteCanvas), transparent: true, opacity: 0.8, alphaTest: 0.1 });
        tankSys.scene.add(new THREE.Points(pGeo, pMat));

        function animateTank() {
            if(activeTab === 'tank') {
                tankSys.controls.update();
                const pos = pGeo.attributes.position.array;
                const col = pGeo.attributes.color.array;
                
                for(let i=0; i<pCount; i++) {
                    if(pData[i].isWater) {
                        if(!isTreated) {
                            // Drop-out physics
                            if (pos[i*3+1] > -7.5) pos[i*3+1] -= 0.08; 
                            col[i*3] = cWater.r; col[i*3+1] = cWater.g; col[i*3+2] = cWater.b;
                        } else {
                            // Emulsion stable suspension
                            pos[i*3+1] += pData[i].yVel;
                            if (pos[i*3+1] > 7.5 || pos[i*3+1] < -7.5) pData[i].yVel *= -1;
                            col[i*3] = cMicelle.r; col[i*3+1] = cMicelle.g; col[i*3+2] = cMicelle.b;
                        }
                    } else {
                        pos[i*3+1] += pData[i].yVel;
                        if (pos[i*3+1] > 7.5 || pos[i*3+1] < -7.5) pData[i].yVel *= -1;
                        col[i*3] = cHydro.r; col[i*3+1] = cHydro.g; col[i*3+2] = cHydro.b;
                    }
                }
                pGeo.attributes.position.needsUpdate = true;
                pGeo.attributes.color.needsUpdate = true;
                tankSys.renderer.render(tankSys.scene, tankSys.camera);
            }
            requestAnimationFrame(animateTank);
        }
        animateTank();

        // 2. Combustion Physics (Flame Kinetics & Efficiency)
        const combSys = setupScene('canvas-combustion');
        combSys.camera.position.set(0, 0, 25);
        combSys.scene.add(new THREE.AmbientLight(0xffffff, 0.4));
        const cLight = new THREE.PointLight(0xf59e0b, 2, 50);
        cLight.position.set(0, 5, 0);
        combSys.scene.add(cLight);

        combSys.scene.add(new THREE.Mesh(
            new THREE.CylinderGeometry(6, 6, 16, 32, 1, true),
            new THREE.MeshPhysicalMaterial({ color: 0x94A3B8, transparent: true, opacity: 0.1, side: THREE.DoubleSide })
        ));
        combSys.scene.add(new THREE.LineSegments(
            new THREE.EdgesGeometry(new THREE.CylinderGeometry(6, 6, 16, 16)),
            new THREE.LineBasicMaterial({ color: 0x64748B, transparent: true, opacity: 0.4 })
        ));
        
        const piston = new THREE.Mesh(
            new THREE.CylinderGeometry(5.8, 5.8, 3, 32),
            new THREE.MeshStandardMaterial({ color: 0x475569, metalness: 0.8 })
        );
        combSys.scene.add(piston);

        const fCount = 800;
        const fGeo = new THREE.BufferGeometry();
        const fPos = new Float32Array(fCount * 3);
        const fCol = new Float32Array(fCount * 3);
        for(let i=0; i<fCount; i++) {
            fPos[i*3] = (Math.random() - 0.5) * 10;
            fPos[i*3+1] = Math.random() * 8;
            fPos[i*3+2] = (Math.random() - 0.5) * 10;
            fCol[i*3] = 1; fCol[i*3+1] = 0.5; fCol[i*3+2] = 0;
        }
        fGeo.setAttribute('position', new THREE.BufferAttribute(fPos, 3));
        fGeo.setAttribute('color', new THREE.BufferAttribute(fCol, 3));
        
        const fMat = new THREE.PointsMaterial({ size: 0.8, vertexColors: true, map: new THREE.CanvasTexture(spriteCanvas), transparent: true, opacity: 0.8, blending: THREE.AdditiveBlending });
        combSys.scene.add(new THREE.Points(fGeo, fMat));

        let cTime = 0;
        function animateCombustion() {
            if(activeTab === 'combustion') {
                combSys.controls.update();
                cTime += isTreated ? 0.1 : 0.03; // Kinetic speed differs based on treatment
                piston.position.y = -4 + Math.sin(cTime) * 3.5;

                const pos = fGeo.attributes.position.array;
                const col = fGeo.attributes.color.array;
                const top = piston.position.y + 1.5;

                for(let i=0; i<fCount; i++) {
                    let y = pos[i*3+1];
                    y -= isTreated ? 0.4 : 0.1; // Flame propagation speed

                    if(y < top) {
                        y = 7 - Math.random(); // Re-ignite at spark
                        pos[i*3] = (Math.random() - 0.5) * 2;
                        pos[i*3+2] = (Math.random() - 0.5) * 2;
                    } else {
                        pos[i*3] *= 1.05; pos[i*3+2] *= 1.05; // Radial expand
                    }
                    pos[i*3+1] = y;

                    // Flame coloration logic
                    if(isTreated) {
                        col[i*3] = 1.0; col[i*3+1] = 0.8; col[i*3+2] = 0.2; // Clean yellow/blue flame
                    } else {
                        col[i*3] = 0.8; col[i*3+1] = 0.2; col[i*3+2] = 0.0; // Sooty, dark red burn
                    }
                }
                fGeo.attributes.position.needsUpdate = true;
                fGeo.attributes.color.needsUpdate = true;
                cLight.intensity = isTreated ? 2.0 : 0.8;

                combSys.renderer.render(combSys.scene, combSys.camera);
            }
            requestAnimationFrame(animateCombustion);
        }
        animateCombustion();

        // 3. Molecule Setup (Tri-tetradecylamine)
        const molSys = setupScene('canvas-molecule');
        molSys.camera.position.set(0, 10, 25);
        molSys.scene.add(new THREE.AmbientLight(0xffffff, 0.6));
        const mLight = new THREE.DirectionalLight(0xffffff, 0.8);
        mLight.position.set(10, 20, 10);
        molSys.scene.add(mLight);

        const mGroup = new THREE.Group();
        const matN = new THREE.MeshPhongMaterial({ color: 0x3b82f6, shininess: 100 }); 
        const matC = new THREE.MeshPhongMaterial({ color: 0x94A3B8, shininess: 60 }); 
        const matBond = new THREE.MeshPhongMaterial({ color: 0x64748b });
        
        mGroup.add(new THREE.Mesh(new THREE.SphereGeometry(1.2, 32, 32), matN));
        const angles = [0, (Math.PI*2)/3, (Math.PI*4)/3]; 
        angles.forEach(angle => {
            let currentPos = new THREE.Vector3(0,0,0);
            for(let i=0; i<6; i++) { // Symbolic tail segments
                const dir = new THREE.Vector3(Math.cos(angle), (i % 2 === 0) ? 0.5 : -0.5, Math.sin(angle)).normalize();
                
                const bond = new THREE.Mesh(new THREE.CylinderGeometry(0.25, 0.25, 2.5, 8), matBond);
                bond.position.copy(currentPos).addScaledVector(dir, 1.25); 
                bond.quaternion.setFromUnitVectors(new THREE.Vector3(0,1,0), dir);
                mGroup.add(bond);

                currentPos.addScaledVector(dir, 2.5);
                const atomC = new THREE.Mesh(new THREE.SphereGeometry(0.8, 32, 32), matC);
                atomC.position.copy(currentPos);
                mGroup.add(atomC);
            }
        });
        mGroup.position.y = -2;
        molSys.scene.add(mGroup);

        function animateMolecule() {
            if(activeTab === 'molecule') {
                molSys.controls.update();
                mGroup.rotation.y += 0.005;
                molSys.renderer.render(molSys.scene, molSys.camera);
            }
            requestAnimationFrame(animateMolecule);
        }
        animateMolecule();

        // Initial Data Load Trigger
        document.getElementById('calculate-btn').click();
    </script>
</body>
</html>
"""

BUY_HTML_OUTPUT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SHIELD-E-MAX | B2B Procurement Portal</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="bg-[#F8FAFC] text-slate-900 antialiased font-sans flex flex-col min-h-screen">
    
    <!-- NAVIGATION -->
    <header class="bg-white border-b border-gray-200">
        <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
            <a href="/" class="flex items-center gap-2">
                <i data-lucide="shield-check" class="w-8 h-8 text-[#0F172A]"></i>
                <span class="text-2xl font-black text-[#0F172A] tracking-tighter">SHIELD-<span class="text-[#10B981]">E</span>-MAX</span>
            </a>
            <div class="text-sm font-bold text-gray-500 uppercase tracking-widest">Industrial B2B Portal</div>
        </nav>
    </header>

    <!-- PROCUREMENT FORM -->
    <main class="flex-grow max-w-4xl mx-auto w-full px-4 py-16">
        <div class="bg-white p-10 md:p-14 rounded-3xl shadow-xl border border-gray-100">
            <div class="text-center mb-10">
                <i data-lucide="building-2" class="w-16 h-16 text-[#0EA5E9] mx-auto mb-4"></i>
                <h1 class="text-4xl font-black text-[#0F172A]">Industrial Procurement</h1>
                <p class="text-gray-600 mt-2 font-medium">Secure your supply of the industry's mandate-ready E20 stabilization matrix.</p>
            </div>

            <form class="space-y-6" onsubmit="event.preventDefault(); alert('Purchase Order Request Submitted Successfully. An engineering representative will contact you within 24 hours.'); window.location.href='/';">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="space-y-2">
                        <label class="font-bold text-gray-700 text-sm">Company Name</label>
                        <input type="text" required class="w-full bg-gray-50 border border-gray-300 p-3 rounded-lg focus:border-[#0EA5E9] focus:bg-white outline-none transition" placeholder="e.g. Bharat Petroleum">
                    </div>
                    <div class="space-y-2">
                        <label class="font-bold text-gray-700 text-sm">Contact Email</label>
                        <input type="email" required class="w-full bg-gray-50 border border-gray-300 p-3 rounded-lg focus:border-[#0EA5E9] focus:bg-white outline-none transition" placeholder="procurement@company.com">
                    </div>
                </div>

                <div class="space-y-2">
                    <label class="font-bold text-gray-700 text-sm">Target Monthly E20 Fuel Volume (Liters)</label>
                    <div class="relative">
                        <i data-lucide="container" class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400"></i>
                        <input type="number" required class="w-full bg-gray-50 border border-gray-300 pl-12 p-3 rounded-lg focus:border-[#0EA5E9] focus:bg-white outline-none transition font-bold" placeholder="e.g. 500000">
                    </div>
                    <p class="text-xs text-gray-500 font-medium mt-1">Based on optimal 1,200 PPM treat rate, our system will calculate exact additive requirements.</p>
                </div>

                <div class="space-y-2">
                    <label class="font-bold text-gray-700 text-sm">Integration Type</label>
                    <select class="w-full bg-gray-50 border border-gray-300 p-3 rounded-lg focus:border-[#0EA5E9] focus:bg-white outline-none transition font-semibold text-gray-700">
                        <option>Depot Bulk Storage Blending</option>
                        <option>In-Line Pipeline Dosing</option>
                        <option>Fleet Bowser Treatment</option>
                        <option>Laboratory Sample / Evaluation</option>
                    </select>
                </div>

                <div class="pt-6">
                    <button type="submit" class="w-full bg-[#10B981] hover:bg-[#059669] text-white py-4 rounded-xl font-bold text-xl shadow-lg transition-all flex justify-center items-center gap-2">
                        <i data-lucide="send"></i> Submit Procurement Request
                    </button>
                    <p class="text-center text-xs text-gray-400 mt-4">By submitting, you agree to our B2B NDA and industrial safety handling protocols.</p>
                </div>
            </form>
        </div>
    </main>

    <script>lucide.createIcons();</script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def serve_shield_e_max_matrix():
    """Main endpoint serving the landing page and 3D simulations."""
    return MAIN_HTML_OUTPUT

@app.get("/buy", response_class=HTMLResponse)
async def serve_buy_portal():
    """Endpoint serving the B2B purchasing portal."""
    return BUY_HTML_OUTPUT

if __name__ == "__main__":
    # Runs the local development server on port 5000
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")