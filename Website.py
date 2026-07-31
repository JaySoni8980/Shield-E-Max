# IMPORTANT: Save this file exactly as 'app.py' (NOT .html)
# Run from terminal using: python app.py

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Initialize the FastAPI application
app = FastAPI(title="SHIELD-E-MAX Ultimate Portal")

# We store the entire HTML, CSS, and JS for the main page in a single robust string.
MAIN_HTML_OUTPUT = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>SHIELD-E-MAX | Next-Gen E20 Fuel Phase Stabilization</title>
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
    <script src="https://unpkg.com/lucide@latest"></script>

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: { 
                        navy: '#0F172A', 
                        emerald: '#10B981', 
                        teal: '#0EA5E9',
                        slate_bg: '#F8FAFC'
                    },
                    boxShadow: { 
                        'glass': '0 8px 32px 0 rgba(31, 38, 135, 0.07)',
                        'glow': '0 0 20px rgba(16, 185, 129, 0.4)'
                    },
                    animation: {
                        'float': 'float 6s ease-in-out infinite',
                    },
                    keyframes: {
                        float: {
                            '0%, 100%': { transform: 'translateY(0)' },
                            '50%': { transform: 'translateY(-10px)' },
                        }
                    }
                }
            }
        }
    </script>
    
    <style>
        /* Modern Glassmorphism UI */
        .glass-card { 
            background: rgba(255, 255, 255, 0.85); 
            backdrop-filter: blur(12px); 
            -webkit-backdrop-filter: blur(12px); 
            border: 1px solid rgba(255, 255, 255, 0.4); 
            border-radius: 24px; 
        }
        .glass-nav { 
            background: rgba(255, 255, 255, 0.95); 
            backdrop-filter: blur(10px); 
            -webkit-backdrop-filter: blur(10px); 
        }
        
        /* Status Pulse Animation */
        @keyframes pulse-emerald { 
            0%, 100% { opacity: 1; transform: scale(1); } 
            50% { opacity: 0.5; transform: scale(1.2); } 
        }
        .emerald-pulse { animation: pulse-emerald 2s cubic-bezier(0.4, 0, 0.6, 1) infinite; }
        
        /* Custom Scrollbar */
        ::-webkit-scrollbar { width: 8px; background: #F8FAFC; }
        ::-webkit-scrollbar-thumb { background: #CBD5E1; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #94A3B8; }
        
        /* 3D Canvas Handling */
        .sim-canvas { outline: none; width: 100%; height: 100%; display: block; }
        .canvas-container { position: absolute; inset: 0; transition: opacity 0.5s ease-in-out; }
        
        /* Tab Transitions */
        .tab-btn { transition: all 0.3s ease; }
        .tab-btn.active { background: white; color: #0F172A; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
        .tab-btn.inactive { color: #64748B; background: transparent; }
        .tab-btn.inactive:hover { color: #0F172A; }
    </style>
</head>
<body class="bg-slate_bg text-slate-900 antialiased font-sans flex flex-col min-h-screen selection:bg-teal selection:text-white">

    <header class="glass-nav sticky top-0 z-50 w-full border-b border-gray-200 shadow-sm transition-all duration-300" id="navbar">
        <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex items-center justify-between">
            <a href="#" class="flex items-center gap-3 group">
                <div class="bg-navy p-2 rounded-xl group-hover:bg-teal transition-colors">
                    <i data-lucide="shield-check" class="w-6 h-6 text-white"></i>
                </div>
                <span class="text-2xl md:text-3xl font-black text-navy tracking-tighter">SHIELD-<span class="text-emerald">E</span>-MAX</span>
            </a>
            
            <div class="hidden lg:flex items-center gap-8 text-sm font-bold text-gray-500 uppercase tracking-wide">
                <a href="#overview" class="hover:text-emerald transition-colors">Overview</a>
                <a href="#about" class="hover:text-emerald transition-colors">The Matrix</a>
                <a href="#simulations" class="hover:text-emerald transition-colors">Digital Twins</a>
                <a href="#calculator" class="hover:text-emerald transition-colors">Economics</a>
            </div>

            <div class="flex items-center gap-4">
                <div class="hidden md:flex items-center gap-2 border border-gray-200 px-4 py-2 rounded-full bg-white shadow-sm">
                    <span class="w-3 h-3 rounded-full bg-emerald emerald-pulse shadow-glow"></span>
                    <span class="text-xs font-black text-gray-700 tracking-wider">SYSTEM ONLINE</span>
                </div>
                <!-- Links to the separate Python route -->
                <a href="/buy" target="_blank" class="bg-emerald text-white px-6 py-2.5 rounded-xl text-sm font-black shadow-lg shadow-emerald/30 hover:bg-emerald/90 hover:shadow-xl hover:-translate-y-0.5 transition-all flex items-center gap-2">
                    <i data-lucide="shopping-cart" class="w-4 h-4"></i> Procure Now
                </a>
            </div>
        </nav>
    </header>

    <main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full py-12 space-y-32 overflow-hidden">

        <section id="overview" class="grid grid-cols-1 lg:grid-cols-12 items-center gap-12 pt-8 relative">
            <!-- Background Decorative Elements -->
            <div class="absolute top-0 right-0 -z-10 w-96 h-96 bg-teal/10 rounded-full blur-3xl mix-blend-multiply"></div>
            <div class="absolute bottom-0 left-0 -z-10 w-72 h-72 bg-emerald/10 rounded-full blur-3xl mix-blend-multiply"></div>

            <div class="lg:col-span-7 space-y-8 relative z-10">
                <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-teal/10 border border-teal/20 text-teal font-black text-xs uppercase tracking-widest">
                    <i data-lucide="zap" class="w-4 h-4"></i> Disrupting E20 Stability
                </div>
                <h1 class="text-6xl md:text-8xl font-black tracking-tighter text-navy leading-[0.95]">
                    Next-Gen <br> E20 Fuel <br> <span class="text-transparent bg-clip-text bg-gradient-to-r from-teal to-emerald">Stabilization.</span>
                </h1>
                <p class="text-xl text-gray-600 font-medium max-w-2xl leading-relaxed">
                    SHIELD-E-MAX is a mandate-ready chemical matrix designed to bridge high-ethanol gasoline blends. Formulated with sterically hindered alkyl-amines for complete <span class="font-bold text-emerald border-b-2 border-emerald/30">20% ethanol blend protection</span>, dynamic pH buffering, and zero-soot combustion.
                </p>
                <div class="flex flex-col sm:flex-row items-center gap-4 pt-4">
                    <a href="#simulations" class="w-full sm:w-auto flex items-center justify-center gap-2 bg-navy text-white px-8 py-4 rounded-xl font-bold text-lg shadow-xl shadow-navy/20 hover:shadow-2xl hover:bg-navy/90 transition-all group">
                        <i data-lucide="cpu" class="w-5 h-5 group-hover:rotate-12 transition-transform"></i> Launch Digital Twins
                    </a>
                    <a href="#calculator" class="w-full sm:w-auto flex items-center justify-center gap-2 bg-white text-navy border-2 border-gray-200 px-8 py-4 rounded-xl font-bold text-lg hover:border-navy transition-all shadow-sm">
                        <i data-lucide="calculator" class="w-5 h-5"></i> ROI Calculator
                    </a>
                </div>
            </div>

            <!-- The 70:20:10 Disruption Card -->
            <div class="lg:col-span-5 glass-card p-8 md:p-10 shadow-glass border-t-4 border-t-teal relative z-10 animate-float">
                <div class="absolute -right-6 -top-6 text-[150px] text-gray-100 opacity-40 pointer-events-none select-none">
                    <i data-lucide="flask-conical"></i>
                </div>
                <h3 class="text-2xl font-black text-navy flex items-center gap-3 mb-8 relative z-10">
                    <span class="bg-emerald/10 text-emerald p-2 rounded-lg"><i data-lucide="activity"></i></span>
                    The 70:20:10 Matrix
                </h3>
                
                <div class="space-y-6 relative z-10">
                    <!-- Component 1 -->
                    <div class="group bg-white/50 p-4 rounded-2xl border border-gray-100 flex items-start gap-4 hover:bg-white transition-colors cursor-default">
                        <div class="bg-blue-50 p-3 rounded-xl shadow-sm text-blue-500 group-hover:scale-110 transition-transform"><i data-lucide="shield" class="w-6 h-6"></i></div>
                        <div>
                            <h4 class="font-bold text-navy text-base">70% Amine Buffer (Phase Shield)</h4>
                            <p class="text-sm text-gray-500 font-medium mt-1 leading-snug">Sterically cages water clusters, preventing phase separation for >90 days.</p>
                        </div>
                    </div>
                    <!-- Component 2 -->
                    <div class="group bg-white/50 p-4 rounded-2xl border border-gray-100 flex items-start gap-4 hover:bg-white transition-colors cursor-default">
                        <div class="bg-teal-50 p-3 rounded-xl shadow-sm text-teal-500 group-hover:scale-110 transition-transform"><i data-lucide="combine" class="w-6 h-6"></i></div>
                        <div>
                            <h4 class="font-bold text-navy text-base">20% DMC (Co-Solvent Bridge)</h4>
                            <p class="text-sm text-gray-500 font-medium mt-1 leading-snug">Reduces miscibility gap tension, providing localized oxygen for a clean burn.</p>
                        </div>
                    </div>
                    <!-- Component 3 -->
                    <div class="group bg-white/50 p-4 rounded-2xl border border-gray-100 flex items-start gap-4 hover:bg-white transition-colors cursor-default">
                        <div class="bg-orange-50 p-3 rounded-xl shadow-sm text-orange-500 group-hover:scale-110 transition-transform"><i data-lucide="flame" class="w-6 h-6"></i></div>
                        <div>
                            <h4 class="font-bold text-navy text-base">10% DTBP (Kinetic Restorer)</h4>
                            <p class="text-sm text-gray-500 font-medium mt-1 leading-snug">Homolytic radical cleavage accelerates flame speed, yielding +4.2% ΔBTE gain.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section id="about" class="relative">
            <div class="absolute inset-0 bg-navy rounded-[3rem] -skew-y-2 transform origin-top-left -z-10"></div>
            <div class="bg-navy p-10 md:p-20 rounded-[3rem] shadow-2xl text-white relative overflow-hidden">
                <!-- Decorative background grid -->
                <div class="absolute inset-0 opacity-10 bg-[linear-gradient(rgba(255,255,255,0.1)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.1)_1px,transparent_1px)] bg-[size:40px_40px]"></div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-16 relative z-10">
                    <div class="space-y-6">
                        <span class="text-emerald font-black tracking-widest text-sm uppercase">The Mandate Problem</span>
                        <h2 class="text-4xl md:text-5xl font-black tracking-tight leading-tight">Bridging India's E20 Engine Gap</h2>
                        <p class="text-lg text-gray-300 font-medium leading-relaxed">
                            As India shifts to a mandatory 20% ethanol blend (E20) to ensure energy security, ~85% of legacy vehicles face severe operational risks. Ethanol's hygroscopic nature pulls water from the air, causing <span class="text-white font-bold">Phase Separation</span>—where a corrosive, watery mixture sinks to the bottom of the fuel tank, rusting metal components and stalling engines.
                        </p>
                        <p class="text-lg text-gray-300 font-medium leading-relaxed">
                            Standard competitive additives use passive detergents that require massive doses and add ₹10–15 per liter to the consumer. SHIELD-E-MAX solves this chemically at the molecular level.
                        </p>
                    </div>
                    
                    <div class="space-y-8 flex flex-col justify-center">
                        <div class="flex items-start gap-4">
                            <div class="bg-white/10 p-4 rounded-2xl"><i data-lucide="check-circle-2" class="w-8 h-8 text-emerald"></i></div>
                            <div>
                                <h4 class="font-bold text-xl text-white mb-1">ASTM Validated Passivation</h4>
                                <p class="text-gray-400 font-medium">Actively passes ASTM D665/D130 for severe rust and copper corrosion inhibition. It doesn't just clean; it protects.</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <div class="bg-white/10 p-4 rounded-2xl"><i data-lucide="trending-down" class="w-8 h-8 text-teal"></i></div>
                            <div>
                                <h4 class="font-bold text-xl text-white mb-1">Disruptive 1:150 Treat Rate</h4>
                                <p class="text-gray-400 font-medium">Algorithmic dosing targets a highly potent 1,200 PPM treat rate. A fraction of the volume is needed compared to legacy detergents.</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-4">
                            <div class="bg-white/10 p-4 rounded-2xl"><i data-lucide="factory" class="w-8 h-8 text-blue-400"></i></div>
                            <div>
                                <h4 class="font-bold text-xl text-white mb-1">Industrial & Fleet Scalability</h4>
                                <p class="text-gray-400 font-medium">Designed for in-line terminal doping and large-scale depot batch mixing. Ready for B2B procurement today.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section id="simulations" class="space-y-8">
            <div class="text-center max-w-4xl mx-auto space-y-4">
                <div class="inline-block p-4 bg-white rounded-3xl shadow-sm border border-gray-100 mb-2">
                    <i data-lucide="monitor-play" class="w-10 h-10 text-teal"></i>
                </div>
                <h2 class="text-4xl md:text-6xl font-black text-navy tracking-tight">Interactive Digital Twins</h2>
                <p class="text-xl text-gray-600 font-medium">Explore the physical chemistry of the SHIELD-E-MAX 70:20:10 matrix through our live WebGL physics engines.</p>
            </div>

            <!-- Simulation Controls Dashboard -->
            <div class="glass-card shadow-glass p-4 md:p-6 flex flex-col lg:flex-row gap-6 items-center justify-between border-2 border-gray-100">
                <!-- Tab Buttons -->
                <div class="flex items-center gap-2 bg-gray-100/80 p-1.5 rounded-2xl border border-gray-200 flex-wrap w-full lg:w-auto">
                    <button onclick="switchSim('tank')" id="btn-tank" class="tab-btn active flex-1 md:flex-none px-6 py-3 rounded-xl font-bold text-sm flex items-center justify-center gap-2">
                        <i data-lucide="database"></i> Tank Phase
                    </button>
                    <button onclick="switchSim('combustion')" id="btn-combustion" class="tab-btn inactive flex-1 md:flex-none px-6 py-3 rounded-xl font-bold text-sm flex items-center justify-center gap-2">
                        <i data-lucide="flame-kindling"></i> Engine Kinetics
                    </button>
                    <button onclick="switchSim('molecule')" id="btn-molecule" class="tab-btn inactive flex-1 md:flex-none px-6 py-3 rounded-xl font-bold text-sm flex items-center justify-center gap-2">
                        <i data-lucide="atom"></i> C14 Molecule
                    </button>
                </div>
                
                <!-- State Toggle Switch -->
                <div class="flex items-center justify-center gap-4 w-full lg:w-auto bg-white px-6 py-3 rounded-2xl border-2 border-gray-100 shadow-sm">
                    <span class="text-sm font-black text-gray-400 uppercase tracking-widest" id="lbl-untreated">Untreated E20</span>
                    
                    <label class="relative inline-flex items-center cursor-pointer">
                        <input type="checkbox" id="sim-toggle" class="sr-only peer" checked onchange="updateSimulationState()">
                        <div class="w-16 h-8 bg-gray-300 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-8 peer-checked:after:border-white after:content-[''] after:absolute after:top-[4px] after:left-[4px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-6 after:w-6 after:transition-all peer-checked:bg-emerald shadow-inner"></div>
                    </label>
                    
                    <span class="text-sm font-black text-emerald uppercase tracking-widest" id="lbl-treated">Treated with SEM</span>
                </div>
            </div>

            <!-- The 3D Canvas Container -->
            <div class="h-[600px] rounded-[2.5rem] overflow-hidden relative shadow-2xl bg-[#0B1121] border-4 border-gray-800 ring-4 ring-gray-100">
                
                <!-- View 1: Storage Tank Physics -->
                <div id="view-tank" class="canvas-container opacity-100 z-10">
                    <div class="absolute top-6 left-6 right-6 md:right-auto z-20 bg-slate-900/80 backdrop-blur-md px-6 py-4 rounded-2xl border border-slate-700 shadow-2xl">
                        <h3 class="font-black text-white text-lg flex items-center gap-2"><i data-lucide="waves" class="text-teal"></i> Storage Tank Physics</h3>
                        <p id="tank-desc" class="text-sm font-bold text-emerald mt-1">Stable Isotropic Micro-Emulsion. Water completely encapsulated by Micelles.</p>
                        <div class="mt-4 flex flex-wrap gap-3 text-xs font-bold text-slate-300">
                            <span class="flex items-center gap-1"><div class="w-3 h-3 rounded-full bg-[#14b8a6]"></div> Hydrocarbon Base</span>
                            <span class="flex items-center gap-1"><div class="w-3 h-3 rounded-full bg-[#ef4444]"></div> Free Water</span>
                            <span class="flex items-center gap-1" id="leg-micelle"><div class="w-3 h-3 rounded-full bg-[#10B981]"></div> Shield-E-Max Micelles</span>
                        </div>
                        <p class="text-[10px] text-slate-500 mt-4 uppercase tracking-widest"><i class="fa-solid fa-rotate mr-1"></i> Drag to rotate environment</p>
                    </div>
                    <canvas id="canvas-tank" class="sim-canvas"></canvas>
                </div>

                <!-- View 2: Cylinder Combustion -->
                <div id="view-combustion" class="canvas-container opacity-0 z-0">
                    <div class="absolute top-6 left-6 right-6 md:right-auto z-20 bg-slate-900/80 backdrop-blur-md px-6 py-4 rounded-2xl border border-slate-700 shadow-2xl">
                        <h3 class="font-black text-white text-lg flex items-center gap-2"><i data-lucide="flame" class="text-orange-500"></i> Engine Cylinder Kinetics</h3>
                        <p id="comb-desc" class="text-sm font-bold text-emerald mt-1">DTBP Radicals active. Accelerated flame speed yielding +4.2% BTE gain.</p>
                        <div class="mt-4 grid grid-cols-2 gap-4">
                            <div class="bg-slate-800 p-2 rounded-lg text-center border border-slate-700">
                                <span class="text-[10px] text-slate-400 uppercase tracking-wider block">Flame Temp</span>
                                <span class="text-sm font-black text-white" id="stat-temp">Optimized</span>
                            </div>
                            <div class="bg-slate-800 p-2 rounded-lg text-center border border-slate-700">
                                <span class="text-[10px] text-slate-400 uppercase tracking-wider block">Ignition Delay</span>
                                <span class="text-sm font-black text-white" id="stat-delay">Minimized</span>
                            </div>
                        </div>
                    </div>
                    <canvas id="canvas-combustion" class="sim-canvas"></canvas>
                </div>

                <!-- View 3: C14 Molecule -->
                <div id="view-molecule" class="canvas-container opacity-0 z-0">
                    <div class="absolute top-6 left-6 right-6 md:right-auto z-20 bg-slate-900/80 backdrop-blur-md px-6 py-4 rounded-2xl border border-slate-700 shadow-2xl">
                        <h3 class="font-black text-white text-lg flex items-center gap-2"><i data-lucide="dna" class="text-blue-400"></i> Tri-tetradecylamine Buffer</h3>
                        <p class="text-sm font-bold text-slate-300 mt-1">The primary active ingredient (70% vol) of SHIELD-E-MAX.</p>
                        <ul class="mt-3 text-xs font-semibold text-slate-400 space-y-1 ml-4 list-disc marker:text-teal">
                            <li><span class="text-blue-400">Blue Node:</span> Nitrogen core provides dynamic pH buffering.</li>
                            <li><span class="text-gray-300">Grey Chains:</span> Triple C14 Alkyl tails create steric hindrance.</li>
                        </ul>
                        <p class="text-[10px] text-slate-500 mt-4 uppercase tracking-widest">Drag to rotate 360° • Scroll to Zoom</p>
                    </div>
                    <canvas id="canvas-molecule" class="sim-canvas"></canvas>
                </div>

            </div>
        </section>

        <section id="calculator" class="space-y-12">
            <div class="text-center max-w-3xl mx-auto space-y-4">
                <div class="inline-block p-4 bg-teal rounded-3xl shadow-lg shadow-teal/30 mb-2">
                    <i data-lucide="bar-chart-3" class="w-10 h-10 text-white"></i>
                </div>
                <h2 class="text-4xl md:text-6xl font-black text-navy tracking-tight">Economic Feasibility</h2>
                <p class="text-xl text-gray-700 font-medium">
                    Input your batch details below. Our proprietary algorithm will calculate exact dosing requirements and prove that SHIELD-E-MAX adds negligible cost to the consumer.
                </p>
            </div>
            
            <div class="glass-card shadow-glass p-8 md:p-12 grid grid-cols-1 lg:grid-cols-12 gap-12 border-2 border-gray-100">
                <!-- Input Form -->
                <div class="lg:col-span-5 space-y-8">
                    <h3 class="text-2xl font-black text-navy flex items-center gap-2 border-b-2 border-gray-100 pb-4">
                        <i data-lucide="settings-2" class="text-emerald"></i> Input Parameters
                    </h3>
                    
                    <div class="space-y-2">
                        <label class="font-bold text-gray-600 text-sm uppercase tracking-wider">Fuel Batch Volume (Liters)</label>
                        <div class="relative group">
                            <i data-lucide="container" class="absolute left-4 top-1/2 -translate-y-1/2 w-6 h-6 text-gray-400 group-focus-within:text-teal transition-colors"></i>
                            <input type="number" id="input-volume" value="10000" class="w-full bg-gray-50 border-2 border-gray-200 pl-14 pr-4 py-4 rounded-2xl font-black text-xl text-navy focus:border-teal focus:bg-white transition-all outline-none shadow-inner hover:border-gray-300">
                        </div>
                    </div>
                    
                    <div class="space-y-2">
                        <label class="font-bold text-gray-600 text-sm uppercase tracking-wider">Target Ethanol Blend (%)</label>
                        <div class="flex items-center gap-4 bg-gray-50 border-2 border-gray-200 rounded-2xl p-3 shadow-inner hover:border-gray-300 transition-colors">
                            <input type="range" id="input-blend" min="5" max="30" value="20" class="flex-1 accent-teal h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer" oninput="document.getElementById('blend-val-display').innerText = 'E' + this.value">
                            <span id="blend-val-display" class="font-black text-navy text-xl w-16 text-center bg-white py-1 rounded-lg shadow-sm border border-gray-100">E20</span>
                        </div>
                    </div>
                    
                    <div class="space-y-2">
                        <label class="font-bold text-gray-600 text-sm uppercase tracking-wider">Dosing Ratio (Optimal 1:150)</label>
                        <div class="relative group">
                            <i data-lucide="percent" class="absolute left-4 top-1/2 -translate-y-1/2 w-6 h-6 text-gray-400 group-focus-within:text-teal transition-colors"></i>
                            <input type="number" id="input-rate" value="150" class="w-full bg-gray-50 border-2 border-gray-200 pl-14 pr-4 py-4 rounded-2xl font-black text-xl text-navy focus:border-teal focus:bg-white transition-all outline-none shadow-inner hover:border-gray-300">
                        </div>
                        <p class="text-xs font-semibold text-emerald ml-1">1 part additive per 150 parts Ethanol.</p>
                    </div>
                    
                    <button id="calculate-btn" class="w-full bg-navy text-white py-5 rounded-2xl font-black text-xl shadow-xl shadow-navy/20 hover:shadow-2xl hover:-translate-y-1 transition-all flex items-center justify-center gap-3">
                        <i data-lucide="activity"></i> Run Financial Audit
                    </button>
                </div>
                
                <!-- Output Results -->
                <div class="lg:col-span-7 bg-navy border-4 border-navy rounded-[2rem] p-8 md:p-10 text-white flex flex-col justify-between relative overflow-hidden shadow-2xl">
                    <!-- Background decor -->
                    <i data-lucide="pie-chart" class="absolute -bottom-10 -right-10 w-64 h-64 text-white/5 pointer-events-none"></i>
                    
                    <div class="flex items-center justify-between border-b border-white/10 pb-6 relative z-10">
                        <h3 class="text-2xl font-black flex items-center gap-3"><i data-lucide="check-circle" class="text-emerald w-8 h-8"></i> Audit Results</h3>
                        <span class="px-4 py-1.5 bg-emerald/20 text-emerald border border-emerald/30 rounded-full text-xs font-black uppercase tracking-widest animate-pulse" id="calc-status">Awaiting Execution</span>
                    </div>
                    
                    <div class="grid grid-cols-2 gap-6 mt-8 relative z-10">
                        <div class="bg-white/5 p-6 rounded-2xl border border-white/10 hover:bg-white/10 transition-colors">
                            <span class="text-xs font-bold text-gray-400 uppercase tracking-widest block mb-2">Required Additive Volume</span>
                            <div class="flex items-baseline gap-2">
                                <span class="text-4xl md:text-5xl font-black text-white" id="output-dose">13.3</span>
                                <span class="font-bold text-gray-400 text-lg">Liters</span>
                            </div>
                        </div>
                        <div class="bg-white/5 p-6 rounded-2xl border border-white/10 hover:bg-white/10 transition-colors">
                            <span class="text-xs font-bold text-gray-400 uppercase tracking-widest block mb-2">Est. Industrial Batch Cost</span>
                            <div class="flex items-baseline gap-2">
                                <span class="text-xl font-bold text-gray-400">₹</span>
                                <span class="text-4xl md:text-5xl font-black text-white" id="output-cost">4,200</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="mt-8 bg-gradient-to-br from-emerald-500/20 to-teal-500/20 border-2 border-emerald-500/30 p-8 rounded-3xl flex flex-col md:flex-row items-center justify-between gap-6 relative z-10">
                         <div>
                             <span class="text-xs font-black text-emerald-400 uppercase tracking-widest block mb-2">Negligible Consumer Impact</span>
                             <div class="flex items-baseline gap-2">
                                 <span class="text-6xl font-black text-white drop-shadow-md" id="output-per-liter">₹0.12</span>
                                 <span class="font-bold text-emerald-200 text-xl">/ Liter</span>
                             </div>
                         </div>
                         <div class="h-16 w-px bg-emerald-500/30 hidden md:block"></div>
                         <div class="text-left md:text-right w-full md:w-auto">
                              <span class="text-xs font-black text-gray-300 uppercase tracking-widest block mb-2">Engine Efficiency Savings</span>
                              <span class="block text-3xl font-black text-teal-400 drop-shadow-md" id="output-savings">₹40,320</span>
                         </div>
                    </div>
                </div>
            </div>
        </section>

    </main>

    <footer class="bg-navy text-gray-400 py-16 border-t border-gray-800 mt-20 relative overflow-hidden">
        <div class="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')] opacity-20 mix-blend-overlay pointer-events-none"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full text-center space-y-6 relative z-10">
            <div class="flex items-center gap-3 justify-center mb-6">
                <div class="bg-white/10 p-2 rounded-xl">
                    <i data-lucide="shield-check" class="w-8 h-8 text-emerald"></i>
                </div>
                <span class="text-3xl font-black tracking-tighter text-white">SHIELD-<span class="text-emerald">E</span>-MAX</span>
            </div>
            <p class="text-base font-medium max-w-xl mx-auto leading-relaxed text-gray-300">
                Proprietary Sterically Hindered Amine Formulation.<br>
                Mandate-Ready Infrastructure for the E20 Transition.
            </p>
            <div class="pt-8 border-t border-gray-800/50 flex flex-col md:flex-row justify-center items-center gap-4 text-sm font-semibold">
                <span>&copy; 2026 Shield-E-Max Thermodynamics Group.</span>
                <span class="hidden md:inline text-gray-600">|</span>
                <a href="/buy" class="text-teal hover:text-emerald transition-colors">B2B Procurement Portal</a>
            </div>
        </div>
    </footer>

    <script>
        // 1. Initialize Lucide Icons
        lucide.createIcons();

        // 2. Financial Calculator Logic
        document.getElementById('calculate-btn').addEventListener('click', function() {
            const btn = this;
            const originalContent = btn.innerHTML;
            btn.innerHTML = '<i data-lucide="loader-2" class="w-6 h-6 animate-spin"></i> Processing Matrix...';
            lucide.createIcons();
            
            // Simulate processing time for UX
            setTimeout(() => {
                const vol = parseFloat(document.getElementById('input-volume').value) || 0;
                const blend = parseFloat(document.getElementById('input-blend').value) || 0;
                const rateRatio = parseFloat(document.getElementById('input-rate').value) || 1;

                if (vol > 0 && blend > 0 && rateRatio > 0) {
                    // Core Math
                    const ethanolVol = vol * (blend / 100.0);
                    const additiveVol = ethanolVol / rateRatio;
                    
                    // Costs based on industrial data
                    const costPerLAdditive = 315.0; // INR
                    const baseBatchCost = additiveVol * costPerLAdditive;
                    const operationalOverhead = (vol / 10000) * 150; // OPEX per 10k L
                    const totalCostBatch = baseBatchCost + operationalOverhead;
                    
                    // Final outputs
                    const costPerLiter = totalCostBatch / vol;
                    const bteBoost = Math.min(5.8, (150.0 / rateRatio) * 4.2); // Efficiency cap
                    const fuelPricePerL = 96.50; // Standard petrol price
                    const efficiencySavings = vol * fuelPricePerL * (bteBoost / 100.0);

                    // Update UI safely
                    document.getElementById('output-dose').innerText = additiveVol.toFixed(1);
                    document.getElementById('output-cost').innerText = Math.round(baseBatchCost).toLocaleString();
                    document.getElementById('output-per-liter').innerText = '₹' + costPerLiter.toFixed(2);
                    document.getElementById('output-savings').innerText = '₹' + Math.round(efficiencySavings).toLocaleString();
                    
                    const statusBadge = document.getElementById('calc-status');
                    statusBadge.innerText = 'Audit Complete';
                    statusBadge.className = 'px-4 py-1.5 bg-emerald text-white border border-emerald-400 rounded-full text-xs font-black uppercase tracking-widest shadow-lg shadow-emerald/30';
                }
                btn.innerHTML = originalContent;
                lucide.createIcons();
            }, 600);
        });

        // 3. Three.js Digital Twin Ecosystem
        let activeSimTab = 'tank';
        let isTreated = true; // State toggle

        // Tab Switching Logic
        function switchSim(tabId) {
            activeSimTab = tabId;
            const tabs = ['tank', 'combustion', 'molecule'];
            
            tabs.forEach(t => {
                // Handle Canvas Visibility
                const view = document.getElementById('view-' + t);
                if (t === tabId) {
                    view.classList.remove('opacity-0', 'z-0');
                    view.classList.add('opacity-100', 'z-10');
                } else {
                    view.classList.add('opacity-0', 'z-0');
                    view.classList.remove('opacity-100', 'z-10');
                }
                
                // Handle Button Styling
                const btn = document.getElementById('btn-' + t);
                if (t === tabId) {
                    btn.classList.remove('inactive');
                    btn.classList.add('active');
                } else {
                    btn.classList.remove('active');
                    btn.classList.add('inactive');
                }
            });
        }

        // Toggle Switch Logic
        function updateSimulationState() {
            const toggle = document.getElementById('sim-toggle');
            isTreated = toggle.checked;
            
            const lblTreated = document.getElementById('lbl-treated');
            const lblUntreated = document.getElementById('lbl-untreated');
            
            // Update labels
            if (isTreated) {
                lblTreated.classList.replace('text-gray-400', 'text-emerald');
                lblUntreated.classList.replace('text-red-500', 'text-gray-400');
                
                // Update Tank Text
                document.getElementById('tank-desc').innerText = "Stable Isotropic Micro-Emulsion. Water completely encapsulated by Micelles.";
                document.getElementById('tank-desc').className = "text-sm font-bold text-emerald mt-1";
                document.getElementById('leg-micelle').style.display = 'flex';
                
                // Update Combustion Text
                document.getElementById('comb-desc').innerText = "DTBP Radicals active. Accelerated flame speed yielding +4.2% BTE gain.";
                document.getElementById('comb-desc').className = "text-sm font-bold text-emerald mt-1";
                document.getElementById('stat-temp').innerText = "Optimized";
                document.getElementById('stat-delay').innerText = "Minimized";
                document.getElementById('stat-temp').className = "text-sm font-black text-emerald";
                document.getElementById('stat-delay').className = "text-sm font-black text-emerald";
                
            } else {
                lblTreated.classList.replace('text-emerald', 'text-gray-400');
                lblUntreated.classList.replace('text-gray-400', 'text-red-500');
                
                // Update Tank Text
                document.getElementById('tank-desc').innerText = "CRITICAL: Phase Separation. Free water dropping out of suspension.";
                document.getElementById('tank-desc').className = "text-sm font-bold text-red-400 mt-1 animate-pulse";
                document.getElementById('leg-micelle').style.display = 'none';
                
                // Update Combustion Text
                document.getElementById('comb-desc').innerText = "WARNING: Ignition delay. Slow, sooty combustion profile.";
                document.getElementById('comb-desc').className = "text-sm font-bold text-orange-400 mt-1";
                document.getElementById('stat-temp').innerText = "Low/Sooty";
                document.getElementById('stat-delay').innerText = "High Lag";
                document.getElementById('stat-temp').className = "text-sm font-black text-orange-400";
                document.getElementById('stat-delay').className = "text-sm font-black text-orange-400";
            }
        }

        // Shared Three.js Setup Helper
        function createScene(canvasId, cameraZ) {
            const canvas = document.getElementById(canvasId);
            const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
            
            // Handle parent resizing automatically
            const parent = canvas.parentElement;
            renderer.setSize(parent.clientWidth, parent.clientHeight, false);
            renderer.setPixelRatio(window.devicePixelRatio);
            
            const camera = new THREE.PerspectiveCamera(45, parent.clientWidth / parent.clientHeight, 0.1, 1000);
            camera.position.z = cameraZ;
            
            const scene = new THREE.Scene();
            
            const controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.enableZoom = true;

            // Global Window Resize Listener
            window.addEventListener('resize', () => {
                if (parent.clientWidth > 0) {
                    camera.aspect = parent.clientWidth / parent.clientHeight;
                    camera.updateProjectionMatrix();
                    renderer.setSize(parent.clientWidth, parent.clientHeight, false);
                }
            });
            
            // Trigger initial resize just in case
            setTimeout(() => { window.dispatchEvent(new Event('resize')); }, 100);

            return { scene, camera, renderer, controls };
        }

        // --- SCENE 1: TANK PHYSICS ---
        const tankSim = createScene('canvas-tank', 35);
        tankSim.camera.position.set(0, 5, 35);
        tankSim.controls.autoRotate = true;
        tankSim.controls.autoRotateSpeed = 1.0;
        tankSim.scene.add(new THREE.AmbientLight(0xffffff, 0.8));

        // Tank Container Geometry
        const tankGeo = new THREE.CylinderGeometry(10, 10, 20, 32, 1, true);
        const tankMat = new THREE.MeshPhysicalMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.1, side: THREE.DoubleSide });
        tankSim.scene.add(new THREE.Mesh(tankGeo, tankMat));
        
        // Tank Edges
        const tankEdges = new THREE.LineSegments(
            new THREE.EdgesGeometry(new THREE.CylinderGeometry(10, 10, 20, 16)),
            new THREE.LineBasicMaterial({ color: 0x0ea5e9, transparent: true, opacity: 0.3 })
        );
        tankSim.scene.add(tankEdges);

        // Particle System
        const pCount = 2500;
        const pGeo = new THREE.BufferGeometry();
        const pPos = new Float32Array(pCount * 3);
        const pCol = new Float32Array(pCount * 3);
        const pData = []; 

        const cHydro = new THREE.Color('#14b8a6'); // Teal base
        const cWater = new THREE.Color('#ef4444'); // Red water
        const cMicelle = new THREE.Color('#10B981'); // Emerald Treated

        for(let i=0; i<pCount; i++) {
            const r = 9.5 * Math.sqrt(Math.random());
            const theta = Math.random() * 2 * Math.PI;
            pPos[i*3] = r * Math.cos(theta);
            pPos[i*3+1] = (Math.random() - 0.5) * 19; // y
            pPos[i*3+2] = r * Math.sin(theta);
            
            pData.push({ 
                yVel: (Math.random() - 0.5) * 0.04, 
                isWater: Math.random() < 0.15 // 15% water
            });
        }
        pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));
        pGeo.setAttribute('color', new THREE.BufferAttribute(pCol, 3));

        // Create a circular sprite for particles
        const spriteCanvas = document.createElement('canvas');
        spriteCanvas.width = 32; spriteCanvas.height = 32;
        const sCtx = spriteCanvas.getContext('2d');
        sCtx.beginPath(); sCtx.arc(16, 16, 14, 0, Math.PI * 2); 
        sCtx.fillStyle = 'white'; sCtx.fill();
        const spriteTexture = new THREE.CanvasTexture(spriteCanvas);
        
        const pMat = new THREE.PointsMaterial({ 
            size: 0.5, vertexColors: true, map: spriteTexture, 
            transparent: true, opacity: 0.9, alphaTest: 0.1 
        });
        tankSim.scene.add(new THREE.Points(pGeo, pMat));

        function renderTank() {
            if(activeSimTab === 'tank') {
                tankSim.controls.update();
                const pos = pGeo.attributes.position.array;
                const col = pGeo.attributes.color.array;
                
                for(let i=0; i<pCount; i++) {
                    if(pData[i].isWater) {
                        if(!isTreated) {
                            // Phase Separation: Water sinks to bottom
                            if (pos[i*3+1] > -9.5) pos[i*3+1] -= 0.05; 
                            col[i*3] = cWater.r; col[i*3+1] = cWater.g; col[i*3+2] = cWater.b;
                        } else {
                            // Encapsulated Micelles: Float safely
                            pos[i*3+1] += pData[i].yVel;
                            if (pos[i*3+1] > 9.5 || pos[i*3+1] < -9.5) pData[i].yVel *= -1;
                            col[i*3] = cMicelle.r; col[i*3+1] = cMicelle.g; col[i*3+2] = cMicelle.b;
                        }
                    } else {
                        // Hydrocarbon base
                        pos[i*3+1] += pData[i].yVel;
                        if (pos[i*3+1] > 9.5 || pos[i*3+1] < -9.5) pData[i].yVel *= -1;
                        col[i*3] = cHydro.r; col[i*3+1] = cHydro.g; col[i*3+2] = cHydro.b;
                    }
                }
                pGeo.attributes.position.needsUpdate = true;
                pGeo.attributes.color.needsUpdate = true;
                tankSim.renderer.render(tankSim.scene, tankSim.camera);
            }
            requestAnimationFrame(renderTank);
        }
        renderTank();

        // --- SCENE 2: COMBUSTION PHYSICS ---
        const combSim = createScene('canvas-combustion', 30);
        combSim.camera.position.set(0, 2, 28);
        combSim.scene.add(new THREE.AmbientLight(0xffffff, 0.3));
        
        const fireLight = new THREE.PointLight(0xf59e0b, 2, 50);
        fireLight.position.set(0, 5, 0);
        combSim.scene.add(fireLight);

        // Cylinder Wall
        combSim.scene.add(new THREE.Mesh(
            new THREE.CylinderGeometry(7, 7, 18, 32, 1, true),
            new THREE.MeshPhysicalMaterial({ color: 0x94A3B8, transparent: true, opacity: 0.15, side: THREE.DoubleSide })
        ));
        combSim.scene.add(new THREE.LineSegments(
            new THREE.EdgesGeometry(new THREE.CylinderGeometry(7, 7, 18, 16)),
            new THREE.LineBasicMaterial({ color: 0x64748B, transparent: true, opacity: 0.5 })
        ));
        
        // Spark plug
        const plug = new THREE.Mesh(new THREE.CylinderGeometry(0.8, 0.8, 3, 16), new THREE.MeshStandardMaterial({ color: 0xcbd5e1, metalness: 0.8 }));
        plug.position.y = 9;
        combSim.scene.add(plug);

        // Moving Piston
        const piston = new THREE.Mesh(
            new THREE.CylinderGeometry(6.8, 6.8, 4, 32),
            new THREE.MeshStandardMaterial({ color: 0x475569, metalness: 0.8, roughness: 0.3 })
        );
        combSim.scene.add(piston);

        // Flame Particles
        const fCount = 1000;
        const fGeo = new THREE.BufferGeometry();
        const fPos = new Float32Array(fCount * 3);
        const fCol = new Float32Array(fCount * 3);
        for(let i=0; i<fCount; i++) {
            fPos[i*3] = (Math.random() - 0.5) * 12;
            fPos[i*3+1] = Math.random() * 10;
            fPos[i*3+2] = (Math.random() - 0.5) * 12;
            fCol[i*3] = 1; fCol[i*3+1] = 0.5; fCol[i*3+2] = 0;
        }
        fGeo.setAttribute('position', new THREE.BufferAttribute(fPos, 3));
        fGeo.setAttribute('color', new THREE.BufferAttribute(fCol, 3));
        
        const fMat = new THREE.PointsMaterial({ 
            size: 1.0, vertexColors: true, map: spriteTexture, 
            transparent: true, opacity: 0.8, blending: THREE.AdditiveBlending 
        });
        combSim.scene.add(new THREE.Points(fGeo, fMat));

        let cTime = 0;
        function renderCombustion() {
            if(activeSimTab === 'combustion') {
                combSim.controls.update();
                // Kinetics change based on treated state
                cTime += isTreated ? 0.08 : 0.03; 
                piston.position.y = -5 + Math.sin(cTime) * 4.0;

                const pos = fGeo.attributes.position.array;
                const col = fGeo.attributes.color.array;
                const pTop = piston.position.y + 2;

                for(let i=0; i<fCount; i++) {
                    let y = pos[i*3+1];
                    y -= isTreated ? 0.3 : 0.1; // Flame speed

                    if(y < pTop) {
                        y = 8 - Math.random() * 2; // Ignite near spark plug
                        pos[i*3] = (Math.random() - 0.5) * 3;
                        pos[i*3+2] = (Math.random() - 0.5) * 3;
                    } else {
                        pos[i*3] *= 1.06; // Radial expand
                        pos[i*3+2] *= 1.06; 
                    }
                    pos[i*3+1] = y;

                    // Color dynamics
                    if(isTreated) {
                        col[i*3] = 1.0; col[i*3+1] = 0.8; col[i*3+2] = 0.2; // Bright yellow/white
                    } else {
                        col[i*3] = 0.8; col[i*3+1] = 0.2; col[i*3+2] = 0.0; // Dark red / sooty
                    }
                }
                fGeo.attributes.position.needsUpdate = true;
                fGeo.attributes.color.needsUpdate = true;
                
                fireLight.intensity = isTreated ? 2.5 : 0.8;
                fireLight.color.setHex(isTreated ? 0xfcd34d : 0xf97316);

                combSim.renderer.render(combSim.scene, combSim.camera);
            }
            requestAnimationFrame(renderCombustion);
        }
        renderCombustion();

        // --- SCENE 3: MOLECULE VIEWER ---
        const molSim = createScene('canvas-molecule', 25);
        molSim.scene.add(new THREE.AmbientLight(0xffffff, 0.7));
        const mLight = new THREE.DirectionalLight(0xffffff, 0.9);
        mLight.position.set(10, 20, 10);
        molSim.scene.add(mLight);

        const mGroup = new THREE.Group();
        const matN = new THREE.MeshPhongMaterial({ color: 0x60a5fa, shininess: 100 }); // Nitrogen (Blue)
        const matC = new THREE.MeshPhongMaterial({ color: 0x94A3B8, shininess: 50 }); // Carbon (Grey)
        const matBond = new THREE.MeshPhongMaterial({ color: 0x475569 });
        
        // Center Nitrogen Node
        mGroup.add(new THREE.Mesh(new THREE.SphereGeometry(1.2, 32, 32), matN));
        
        // Triple C14 Tails
        const angles = [0, (Math.PI*2)/3, (Math.PI*4)/3]; 
        angles.forEach(angle => {
            let currentPos = new THREE.Vector3(0,0,0);
            for(let i=0; i<8; i++) { // Render 8 segments visually for C14
                const dir = new THREE.Vector3(Math.cos(angle), (i % 2 === 0) ? 0.6 : -0.6, Math.sin(angle)).normalize();
                
                const bond = new THREE.Mesh(new THREE.CylinderGeometry(0.3, 0.3, 2.5, 12), matBond);
                bond.position.copy(currentPos).addScaledVector(dir, 1.25); 
                bond.quaternion.setFromUnitVectors(new THREE.Vector3(0,1,0), dir);
                mGroup.add(bond);

                currentPos.addScaledVector(dir, 2.5);
                const atomC = new THREE.Mesh(new THREE.SphereGeometry(0.9, 32, 32), matC);
                atomC.position.copy(currentPos);
                mGroup.add(atomC);
            }
        });
        mGroup.position.y = -2;
        molSim.scene.add(mGroup);

        function renderMolecule() {
            if(activeSimTab === 'molecule') {
                molSim.controls.update();
                mGroup.rotation.y += 0.005;
                mGroup.rotation.x = Math.sin(Date.now() * 0.001) * 0.1; // Gentle bob
                molSim.renderer.render(molSim.scene, molSim.camera);
            }
            requestAnimationFrame(renderMolecule);
        }
        renderMolecule();

    </script>
</body>
</html>
"""

BUY_HTML_OUTPUT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Procure SHIELD-E-MAX</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        body { background: #0F172A; } /* Navy Background for Buy Page */
        .glass-form {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
    </style>
</head>
<body class="text-white antialiased font-sans min-h-screen flex flex-col items-center justify-center p-4 selection:bg-emerald selection:text-white">

    <a href="/" class="absolute top-6 left-6 text-gray-400 hover:text-white flex items-center gap-2 transition-colors font-bold text-sm">
        <i data-lucide="arrow-left" class="w-4 h-4"></i> Return to Portal
    </a>

    <div class="w-full max-w-3xl glass-form rounded-[2.5rem] p-10 md:p-16 shadow-2xl">
        <div class="text-center mb-10">
            <div class="inline-block bg-emerald/20 p-4 rounded-full mb-4 border border-emerald/30">
                <i data-lucide="shield-check" class="w-12 h-12 text-emerald"></i>
            </div>
            <h1 class="text-4xl md:text-5xl font-black tracking-tight mb-2">Industrial Procurement</h1>
            <p class="text-gray-400 font-medium text-lg">Secure your bulk supply of the mandate-ready E20 stabilization matrix.</p>
        </div>

        <form class="space-y-6" onsubmit="event.preventDefault(); alert('Request Received! Our engineering team will contact you within 24 hours to finalize your batch requirements.'); window.location.href='/';">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="space-y-2">
                    <label class="text-sm font-bold text-gray-300 uppercase tracking-widest">Company Name</label>
                    <input type="text" required class="w-full bg-black/30 border border-gray-600 rounded-xl px-4 py-3 text-white focus:border-emerald focus:ring-1 focus:ring-emerald outline-none transition-all placeholder-gray-600" placeholder="e.g. Reliance Petroleum">
                </div>
                <div class="space-y-2">
                    <label class="text-sm font-bold text-gray-300 uppercase tracking-widest">Official Email</label>
                    <input type="email" required class="w-full bg-black/30 border border-gray-600 rounded-xl px-4 py-3 text-white focus:border-emerald focus:ring-1 focus:ring-emerald outline-none transition-all placeholder-gray-600" placeholder="procurement@company.com">
                </div>
            </div>

            <div class="space-y-2">
                <label class="text-sm font-bold text-gray-300 uppercase tracking-widest">Monthly Fuel Treatment Vol. (Liters)</label>
                <div class="relative">
                    <i data-lucide="droplet" class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-500 w-5 h-5"></i>
                    <input type="number" required min="1000" class="w-full bg-black/30 border border-gray-600 rounded-xl pl-12 pr-4 py-3 text-white focus:border-emerald focus:ring-1 focus:ring-emerald outline-none transition-all font-bold text-lg" placeholder="100,000">
                </div>
                <p class="text-xs text-gray-500 font-medium">Algorithm will auto-calculate optimal 1,200 PPM dosing requirement.</p>
            </div>

            <div class="space-y-2">
                <label class="text-sm font-bold text-gray-300 uppercase tracking-widest">Deployment Integration</label>
                <select class="w-full bg-black/30 border border-gray-600 rounded-xl px-4 py-3 text-white focus:border-emerald focus:ring-1 focus:ring-emerald outline-none transition-all font-semibold">
                    <option class="text-gray-900">Refinery / Depot Bulk Blending</option>
                    <option class="text-gray-900">In-Line Pipeline Dosing</option>
                    <option class="text-gray-900">Fleet Tank Treatment</option>
                    <option class="text-gray-900">Laboratory Validation Sample</option>
                </select>
            </div>

            <button type="submit" class="w-full bg-emerald hover:bg-emerald-600 text-white font-black text-xl py-5 rounded-xl shadow-lg shadow-emerald/20 transition-all flex items-center justify-center gap-2 mt-4">
                <i data-lucide="send"></i> Submit Purchase Request
            </button>
            
            <p class="text-center text-xs text-gray-500 mt-6">
                By submitting this form, you agree to the industrial safety & handling NDA.
            </p>
        </form>
    </div>

    <script>lucide.createIcons();</script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    """Serves the massive, single-page highly detailed portal."""
    return MAIN_HTML_OUTPUT

@app.get("/buy", response_class=HTMLResponse)
async def buy_portal():
    """Serves the separate B2B Purchasing page."""
    return BUY_HTML_OUTPUT

if __name__ == "__main__":
    # Ensure uvicorn runs the app on localhost port 8000 to avoid conflicts
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")