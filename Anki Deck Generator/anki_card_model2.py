import random
import genanki



anki_card_model_Ph = genanki.Model(
    # random.randrange(1 << 30, 1 << 31),
    1279500475,
    'Book2_Note_Ph',
    fields=[
        {
            'name': 'Learn',
            'font': 'Arial',
        },
        {
            'name': 'Learn_Note',
            'font': 'Arial',
        },
        {
            'name': 'Speak',
            'font': 'Arial',
        },
        {
            'name': 'Speak_Note',
            'font': 'Arial',
        },        
        {
            'name': 'Audio_Learn',
        },
        {
            'name': 'FileName_Audio_Learn',
            'font': 'Arial',
        },
        {
            'name': 'Audio_Speak',
        },
        {
            'name': 'FileName_Audio_Speak',
            'font': 'Arial',
        },
        {
            'name': 'Image',
        },  
        {
            'name': 'Note',
            'font': 'Arial',
        },              
        {
            'name': 'ID-number',
            'font': 'Arial',
        },
        {
            'name': 'Category',
            'font': 'Arial',
        },        
        {
            'name': 'Speak->Learn',
            'font': 'Arial',
        }
    ],
    
    templates=[
        {
            'name': 'Card 1',
            'qfmt': """
<div id="statusSL" style="position: absolute; font-size: 12px; color: #aaaaaaaa; top: 1px; left: 1px; z-index: 1019;" ></div>
{{#Learn_Note}}
<span class="note">( {{Learn_Note}} )<span>
<br>
{{/Learn_Note}}
<div>
    <div class="inFrame bgYellow">        
        <span id="id_wordL" class="bgYellow word_learned showWordSlowly" style="--ws-delay: 0s; --ws-bcolor: var(--parYellow); --ws-duration: 1.5s;">{{Learn}}</span>
    </div>
</div>

<div class="psound">
<div>
    <a class="replay-buttonMy" id="id_slow1"
        onclick="stopAllAudio(); reDraw('id_wordL', 'showWordSlowly'); playAudioSWeb('{{text:FileName_Audio_Learn}}', 0.6);">
        <svg class="playImageMy" viewBox="0 0 64 64" version="1.1">
            <circle cx="32" cy="32" r="29" />
            <path d="M56.502,32.301l-37.502,20.101l0.329,-40.804l37.173,20.703Z" />
            <rect x="27" y="30" width="12" height="4" fill="lightgray" />
        </svg>
    </a>
</div>    
    &nbsp;&nbsp;&nbsp;    
    <div onclick="stopAllAudio(); reDraw('id_wordL', 'showWordSlowly');" style="margin: 10px 0px; zoom: 1.0;">{{Audio_Learn}}</div>
</div>


<div>
<label style="font-size: 14px;" title="Hint from the past 10 cards" class="chBox">
  <input type="checkbox" id="checkboxH10" name="hintPast10" value="yes" onchange="checkboxH10CH(event);"> hint past 10
</label>

<label style="font-size: 14px;" class="chBox hideinankidroid hideindesk hideinios" title="For Ankiweb: Play the sound of the word being studied when you press the 'Show Answer' button">
  <input type="checkbox" id="checkboxAS" name="ankiweb sound" value="yes" onchange="checkboxASCH(event);" class="hideinankidroid hideindesk hideinios"> answer sound
</label>
</div>



<div class="hintblock" id="hintblock1" style="display: none;">
<div class="spbtnHints">
<button id="btnHint1" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHint2" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHint3" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHint4" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHint5" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHint6" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHint7" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHint8" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHint9" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHint10" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHintLoop" onclick="playAllHintLoop(event)" class="btnHintsLoop">&nbsp;🔊&nbsp;🔁&nbsp;</button>
</div>
</div>

<div style="position: fixed; font-size: 12px; color: #aaaaaaaa; bottom: 1px; left: 1px; z-index: 10000;" >{{Card}}</div>
<div style="position: fixed; font-size: 12px; color: #aaaaaaaa; bottom: 1px; left: 50%; transform: translateX(-50%); z-index: 10000;" >id: {{ID-number}}</div>
<div style="position: fixed; font-size: 12px; color: #aaaaaaaa; bottom: 1px; right: 1px; z-index: 10000;" >{{Category}}</div>


<script> // ***** 251210 reDraw ****************************
// redraws by removing and adding the class again
function reDraw(idel, classname) {
    let el = document.getElementById(idel);
    if(!el) return;    
    el.classList.remove(classname);
    void el.offsetWidth; // for redrawing
    el.classList.add(classname);  
}
// ***** 251210 reDraw ****************************
</script> 


<script> // ***** 251210 audio list player *****************
// === Audio file player ===
// === both individually and as a list ===
window.onHintPlaylistStart = null;
window.onHintPlaylistCancel = null;
window.onHintPlaylistAttention = null;
if(window.audioSWebManager) stopAllAudio();
// Global Audio Manager
if (!window.audioSWebManager) {
    window.audioSWebManager = {        
        audio: null, // Current player
        playlist: [], // Play queue
        currentIndex: 0,
        playlistId: 0, // Playlist ID for tracking relevance
        isPlaying: false,
        loop: false,
        shuffleN: 0, // after how many cycles will the mixture be mixed
        loopN: 0, // current cycle number
                
        initAudio() {
            if (!this.audio) {
                this.audio = new Audio();                
                // Audio event handlers
                this.audio.addEventListener('ended', () => {
                    this.onAudioEnded();
                });                
                this.audio.addEventListener('error', (e) => {
                    console.log('Audio error:', e);
                    this.onAudioEnded();
                });
            }
            return this.audio;
        },
        
        // Normal playback of a single file (cancels the playlist)
        playSingle(filename, speed = 1.0) {            
            this.stop();
            this.playFile(filename, speed); // Play the file
        },
        
        // Playing a file
        playFile(filename, speed = 1.0) {
            if (!filename || filename.trim() === '') return false;
            
            const audio = this.initAudio();  
            audio.pause();
            audio.currentTime = 0;
            audio.src = filename;
            audio.playbackRate = speed;
            
            // Attempting to reproduce
            return audio.play().then(() => {
                this.isPlaying = true;
                return true;
            }).catch(error => {
                console.log('Audio play failed:', error);
                this.isPlaying = false;
                return false;
            });
        },
        
        // Playing a playlist
        playPlaylist(files, loop = false, shuffleN = 0) {          
            this.playlistId++; // Increase the playlist ID to track relevance
            const currentPlaylistId = this.playlistId;            
            this.playlist = files; // Array of objects {filename, speed}
            this.currentIndex = 0;
            this.loop = loop;
            this.shuffleN = shuffleN;
            this.loopN = 0;
            this.isPlaying = true;    
        
            // We start playing the first file
            this.playNextInPlaylist(currentPlaylistId);
        },
        
        // shuffle file blocks
        shuffleBlocks(playlist) {
            // We divide it into blocks and immediately determine which blocks are empty.
            const blocks = [];
            let currentBlock = [];
            let currentBlockHasRealFiles = false;            
            for (let i = 0; i < playlist.length; i++) {
                const item = playlist[i];                
                if (item.filename === ':0') {                    
                    currentBlock.push(item); // Add end of block marker                   
                    // Save a block with information about whether it contains real files
                    blocks.push({
                        items: currentBlock,
                        hasRealFiles: currentBlockHasRealFiles
                    });                    
                    // Reset for the next block
                    currentBlock = [];
                    currentBlockHasRealFiles = false;
                } else {
                    currentBlock.push(item);
                    // Check if the file is real (not a service file)
                    if (!item.filename.startsWith(':')) {
                        currentBlockHasRealFiles = true;
                    }
                }
            }
            
            // Process the last block, if there is one
            if (currentBlock.length > 0) {
                blocks.push({
                    items: currentBlock,
                    hasRealFiles: currentBlockHasRealFiles
                });
            }
            
            // Split into non-empty and empty blocks
            const nonEmptyBlocks = blocks.filter(block => block.hasRealFiles);
            const emptyBlocks = blocks.filter(block => !block.hasRealFiles);
            
            // Shuffle only non-empty blocks if there is more than one
            if (nonEmptyBlocks.length > 1) {                
                for (let i = nonEmptyBlocks.length - 1; i > 0; i--) {
                    const j = Math.floor(Math.random() * (i + 1));
                    [nonEmptyBlocks[i], nonEmptyBlocks[j]] = [nonEmptyBlocks[j], nonEmptyBlocks[i]];
                }
            }
            
            // We collect the results
            const result = [];            
            // Adding shuffled non-empty blocks
            nonEmptyBlocks.forEach(block => {
                result.push(...block.items);
            });            
            // Add empty blocks at the end (usually this is just the final marker)
            emptyBlocks.forEach(block => {
                result.push(...block.items);
            });            
            return result;
        },
        
        
        // Play the next file in the playlist
        playNextInPlaylist(playlistId) {
            // Let's check if this playlist is still relevant
            if (playlistId !== this.playlistId) {
                console.log('Playlist outdated, stopping');
                return;
            }
            
            // Testing the boundaries
            if (this.currentIndex >= this.playlist.length) {
                if (this.loop) {
                    this.currentIndex = 0; // Looping
                    this.loopN += 1;
                    if(this.shuffleN > 0 && this.loopN >= this.shuffleN ) {
                        this.loopN = 0; 
                        this.playlist = this.shuffleBlocks(this.playlist);
                        this.shuffleN = 1;
                        console.log("The playlist blocks are shuffled and will change with each playback.");            
                    }
                } else {
                    this.isPlaying = false;
                    return; // End of playlist
                }
            }
            
            const item = this.playlist[this.currentIndex];
            
            if (item.filename.startsWith('!')) {                
                if (playlistId === this.playlistId) {
                    if (window.onHintPlaylistAttention) window.onHintPlaylistAttention(item.filename.slice(1)); 
                    this.currentIndex++;
                    this.playNextInPlaylist(playlistId);
                }
                return;                
            }
                
            // Checking the pause (file starts with :)
            if (item.filename.startsWith(':')) {
                const delay = parseInt(item.filename.substring(1));
                // end of block file mark (for shuffling)
                // {filename: ':0', speed: 1.0}                 
                if( delay != 0 ) {
                    setTimeout(() => {
                        // Checking that the playlist is still up to date
                        if (playlistId === this.playlistId) {
                            this.currentIndex++;
                            this.playNextInPlaylist(playlistId);
                        }
                    }, delay);
                }                    
                else {
                    if (playlistId === this.playlistId) {
                        this.currentIndex++;
                        this.playNextInPlaylist(playlistId);
                    }
                }
                return;
            }
            
            // Playing a regular file
            this.playFile(item.filename, item.speed || 1.0).then(success => {
                if (success) {
                    // currentIndex will increase after the end of the track (in onAudioEnded)
                } else {
                    // If there is a playback error, move on to the next one
                    if (playlistId === this.playlistId) {
                        this.currentIndex++;
                        this.playNextInPlaylist(playlistId);
                    }
                }
            });
        },
        
        // End of track handler
        onAudioEnded() {
            this.isPlaying = false;
            
            // If there is an active playlist
            if (this.playlist.length > 0 && this.playlistId > 0) {
                this.currentIndex++;
                this.playNextInPlaylist(this.playlistId);
            }
        },
       
        pause() {
            if (this.audio) {
                this.audio.pause();
                this.isPlaying = false;
            }
        },
                
        resume() {
            if (this.audio && !this.isPlaying && this.audio.currentTime > 0) {
                this.audio.play().then(() => {
                    this.isPlaying = true;
                }).catch(console.error);
            }
        },
                
        stop() {
            if (this.audio) {
                this.audio.pause();
                this.audio.currentTime = 0;
                this.audio.src = '';
            }
            
            this.playlist = [];
            this.playlistId = 0;
            this.currentIndex = 0;
            this.isPlaying = false;
        },
        
        // Skip the current track in the playlist
        skip() {
            if (this.playlist.length > 0) {
                if (this.audio) {
                    this.audio.pause();
                    this.audio.currentTime = 0;
                }
                this.currentIndex++;
                this.playNextInPlaylist(this.playlistId);
            }
        },
                
        getStatus() {
            return {
                isPlaying: this.isPlaying,
                playlistId: this.playlistId,
                currentIndex: this.currentIndex,
                playlistLength: this.playlist.length,
                currentTime: this.audio ? this.audio.currentTime : 0,
                duration: this.audio ? this.audio.duration : 0
            };
        }
    };
}



function playAudioSWeb(filename, speed) {
    if (!filename || filename.trim() === "") return;   
    if (window.onHintPlaylistCancel) window.onHintPlaylistCancel(); 
    // Using the manager for single playback
    window.audioSWebManager.playSingle(filename, speed || 1.0);
}

// Function for playing a list of files
function playAudioList(files, loop = false, shuffleN = 0) {    
    /* files - array of objects or strings: ['file1.mp3', 'file2.mp3']
    или
      [
        {filename: '!nameForAttention', speed: 1.0}, // call to the "window.onHintPlaylistAttention" function
        {filename: 'file1.mp3', speed: 1.0},
        {filename: ':1000', speed: 1.0}, // pause 1 second
        {filename: 'file2.mp3', speed: 1.5},
        {filename: ':0', speed: 1.0} // end of block file mark (for shuffling)
      ] 
    shuffleN - after how many cycles will the mixture be mixed    
    */        
    // Normalize the input data
    const normalizedFiles = files.map(item => {
        if (typeof item === 'string') {
            return { filename: item, speed: 1.0 };
        }
        return item;
    });    
    window.audioSWebManager.playPlaylist(normalizedFiles, loop, shuffleN);
}

function stopAllAudio() {
    window.audioSWebManager.stop();
}

function pauseAudio() {
    window.audioSWebManager.pause();
}

function resumeAudio() {
    window.audioSWebManager.resume();
}

// Skip the current track
function skipAudio() {
    window.audioSWebManager.skip();
}

function getAudioStatus() {
    return window.audioSWebManager.getStatus();
}
// ================
// ***** 251210 audio list player *****************
</script> 



<script> // ***** 251210 CardDesign class ******************
/* =================== CardDesign class =================== */
if (!window.CardDesign) {
window.CardDesign = class {
    constructor(cd_id) {
        this.id = cd_id;        
        this.version = "1.0";
        this.platform = this.detectAnkiPlatform();
        this.dataPar = {}; // Parameters for all currently viewed cards       
        this.data = {}; // Data entered on the face of the card        
        this.loadPar(); // Load parameters for all currently viewed cards    
        if(this.isAnswer())
            this.load();
        else
            this.save(); // clear as empty
 
        this.boundSave = this.save.bind(this);
        window.addEventListener("beforeunload", this.boundSave);       
        this.boundSaveIsHidden = this.saveIsHidden.bind(this);
        document.addEventListener("visibilitychange", this.boundSaveIsHidden);
        
        // hide elements not for this platform
        this.hideElementsPlatform();
    }
    
    
    destroy() {        
        window.removeEventListener("beforeunload", this.boundSave);
        document.removeEventListener("visibilitychange", this.boundSaveIsHidden);
    }
    
    isAnswer() {
        let el = document.getElementById("answer");
        if(el) {            
            return true;            
        }        
        return false;        
    }
    
    detectAnkiPlatform() {
        if (typeof pycmd !== "undefined") return "desk";
        if (typeof AnkiDroidJS !== "undefined") return "ankidroid";
        if (document.getElementById("qa_box")) return "ankiweb";
        return "ios";
    }
    
    save() {       
        try {            
            window.localStorage.setItem(
                "CardDesign_" + this.id,
                JSON.stringify({
                    data: this.data       
                })
            );
        } catch (e) {
            console.log("CardDesign.save error:", e);
        }
    }
    
    saveIsHidden() {
        if (document.hidden) this.save();    
    }

    load() {
        try {            
            const saved = window.localStorage.getItem("CardDesign_" + this.id);
            if (!saved) return;
            const obj = JSON.parse(saved);
            if (obj.data) this.data = obj.data;
        } catch (e) {
            console.log("CardDesign.load error:", e);
        }
    }
    
    savePar() {       
        try {
            window.localStorage.setItem(
                "CardDesign_Par_" + this.id,
                JSON.stringify({
                    data: this.dataPar     
                })
            );
        } catch (e) {
            console.log("CardDesign.savePar error:", e);
        }
    }

    loadPar() {
        try {
            const saved = window.localStorage.getItem("CardDesign_Par_" + this.id);
            if (!saved) return;
            const obj = JSON.parse(saved);
            if (obj.data) this.dataPar = obj.data;
        } catch (e) {
            console.log("CardDesign.loadPar error:", e);
        }
    }

    log(msg) {
        console.log(`[CardDesign v=${this.version}, app=${this.platform}] ${msg}`);
    }
    
    showAnswer() {
        if (this.platform == "desk") {            
            pycmd("ans");
        }
        else if (this.platform == "ankidroid") {
            window.showAnswer();
        }
        else if (this.platform == "ankiweb") {
            const btn = document.querySelector("#ansarea .btn");            
            if (btn) btn.click();
            else this.log("ERROR: Button not found in showAnswer()");
        }
    }    
    

    setData(key, value) {
        this.data[key] = value;
        this.save();
    }

    getData(key) {
        return this.data[key];
    }
    
    setPar(key, value) {
        this.dataPar[key] = value;
        this.savePar();
    }

    getPar(key) {
        return this.dataPar[key];
    }
    
    // hide elements not for this app or party
    hideElementsPlatform() {
        let Elements = null;
        if( this.platform == "desk") {
            Elements = document.getElementsByClassName('hideindesk');            
            for (let elem of Elements) elem.style= "display: none";                            
        }
        else if( this.platform == "ankidroid") {
            Elements = document.getElementsByClassName('hideinankidroid');
            for (let elem of Elements) elem.style= "display: none";
        }        
        else if( this.platform == "ankiweb") {
            Elements = document.getElementsByClassName('hideinankiweb');
            for (let elem of Elements) elem.style= "display: none";            
        }
        else if( this.platform == "ios") {
            Elements = document.getElementsByClassName('hideinios');
            for (let elem of Elements) elem.style= "display: none";            
        }
        
        if(this.isAnswer()) {
            Elements = document.getElementsByClassName('hideisback');
            for (let elem of Elements) elem.style= "display: none";            
        }
        else {            
            Elements = document.getElementsByClassName('hideisfront');
            for (let elem of Elements) elem.style= "display: none";            
        }
    }    
}}
/* ========↑↑↑======== CardDesign class ========↑↑↑======== */
// ***** 251210 CardDesign class ******************
</script> 





<script> // ***** 251210 HintQueue class *******************
/* =================== HintQueue class =================== */
if (!window.HintQueue) {
window.HintQueue = class {
    constructor(limit = 10) {
        this.limit = limit;
        this.items = []; // [{word: "...", trans: "...", fnword: "...", fntrans: "..."}]
    }

    add(word, trans, fnword, fntrans) {
        if (!word) return;    
        // We delete the duplicate if there is one.
        this.items = this.items.filter(item =>
            !(item.word === word && item.trans === trans)
        );    
        // Add to the end
        this.items.push({ word, trans, fnword, fntrans });    
        // Limiting the queue size
        if (this.items.length > this.limit) {
            this.items.shift();
        }
    }

    get(i) {
        if (i < 0 || i >= this.items.length) return ["", ""];
        const { word, trans, fnword, fntrans } = this.items[i];
        return [word, trans, fnword, fntrans];
    }

    size() {
        return this.items.length;
    }

    /* Returns a NEW array of shuffled pairs */
    getShuffled() {
        const arr = [...this.items];
        for (let i = arr.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        return arr;
    }
}}
/* ========↑↑↑======== HintQueue class ========↑↑↑======== */
// ***** 251210 HintQueue class *******************
</script> 




<script> // ======================= MAIN ============================

checkedCheckboxH10 = false;
function checkboxH10CH(event){         
    let ch = event.target.checked; 
    checkedCheckboxH10 = ch;    
    let elH10 = document.getElementById("hintblock1");
    if(checkedCheckboxH10) {
        if(elH10) elH10.style.display = "flex";   
    }
    else {
        if(elH10) elH10.style.display = "none";    
    }    
    window.cd.setPar("checkboxH10"+`{{Card}}`, String(ch)); 
    fillHintButtons();   
}


checkedCheckboxAS = false;
function checkboxASCH(event){     
    let ch = event.target.checked; 
    checkedCheckboxAS = ch;    
    window.cd.setPar("checkboxAS", String(ch));    
}


function setcheckboxAll(){
    if(window.cd) {
        try {
            let ch = window.cd.getPar("checkboxH10"+`{{Card}}`);            
            let el = document.getElementById("checkboxH10");            
            if(el) {
                let elH10 = document.getElementById("hintblock1");
                if(ch == "true") {
                    el.checked = true;  
                    checkedCheckboxH10 = true;
                    if(elH10) elH10.style.display = "flex";
                }
                else {                    
                    el.checked = false; 
                    checkedCheckboxH10 = false;  
                    if(elH10) elH10.style.display = "none";                  
                }                    
            } 
        }
        catch(e) {}
        
        try {
            let ch = window.cd.getPar("checkboxAS");            
            let el = document.getElementById("checkboxAS");            
            if(el) {                                  
                if(ch == "true") {
                    el.checked = true;  
                    checkedCheckboxAS = true;                    
                }
                else {                    
                    el.checked = false; 
                    checkedCheckboxAS = false;                    
                }                    
            } 
        }
        catch(e) {}
    }
}


// === HintButtons ===
// Function of outputting words to buttons (after shuffling) 
function fillHintButtons() {
    const shuffled = hintStore.getShuffled();

    const btns = document.querySelectorAll(".hintblock .btnHints");

    for (let i = 0; i < btns.length; i++) {
        const btn = btns[i];

        if (i < shuffled.length) {
            btn.dataset.word = shuffled[i].word;
            btn.dataset.trans = shuffled[i].trans;
            btn.dataset.idwt = shuffled[i].word + "#" + shuffled[i].trans;
            btn.dataset.fnword = String(shuffled[i].fnword);
            btn.dataset.fntrans = String(shuffled[i].fntrans); 
            btn.innerHTML = shuffled[i].word;             
        } else {
            // if really less than 10 words
            btn.dataset.word = "";
            btn.dataset.trans = "";
            btn.dataset.idwt = "";
            btn.dataset.fnword = "";
            btn.dataset.fntrans = "";            
            btn.innerHTML = "";        
        }
        btn.classList.remove("errtrans");
        btn.classList.remove("truetrans");
        btn.classList.remove("playAttention"); 
    }
}

// adding a new word
function addNewHint(word_Speak, word_Learn, fn_word_Speak, fn_word_Learn) {
    hintStore.add(word_Speak, word_Learn, fn_word_Speak, fn_word_Learn);    
    fillHintButtons();
}


document.removeEventListener('click', window.clickHintButtons);
window.clickHintButtons = function (event) {
    const btn = event.target.closest(".btnHints");
    if (!btn) return;   

    const word = btn.dataset.word;
    const trans = btn.dataset.trans;
    const fnword = btn.dataset.fnword;    
    const fntrans = btn.dataset.fntrans;
    if (!word) return;

    // reveal the translation
    btn.innerHTML = `<b>${trans}</b><br>${word}`;
    let word_Speak = `{{text:Speak}}`;
    // we check the correctness
    if (word !== word_Speak) {   // variable of the current correct translation
        btn.classList.add("errtrans");
    }
    else {
        btn.classList.add("truetrans");          
    }
    
    // sound fntrans fnword
    if(fntrans != "") {
        try{
            if (window.onHintPlaylistCancel) window.onHintPlaylistCancel();
            playAudioList([fntrans, fnword]); 
        }
        catch(er){}
    } 
}
document.addEventListener('click', window.clickHintButtons);

// =====================


// play all the prompts in a loop
function playAllHintLoop(event) {
    let elB = event.target;
    if(elB.classList.contains("active")) {
        elB.classList.remove('active');
        if (window.onHintPlaylistCancel) window.onHintPlaylistCancel();
        stopAllAudio();
        return;
    }
    const btns = document.querySelectorAll(".hintblock .btnHints");
    let listP = [];
    
    for (let i = 0; i < btns.length; i++) {
        const btn = btns[i];         
        if(btn.dataset.trans && btn.dataset.trans.trim() !== "") {
            // Adding files to the list
            listP.push(
                {filename: '!'+ String(btn.dataset.idwt), speed: 1.0}, // call to the "window.onHintPlaylistAttention" function
                {filename: btn.dataset.fntrans || '', speed: 1.0},
                {filename: btn.dataset.fnword || '', speed: 1.0},
                {filename: ':1000', speed: 1.0}, // pause 1 second 
                {filename: ':0', speed: 1.0} // end of block file mark (for shuffling)
            );
        }
    }
    
    // Filter empty files (just in case)
    listP = listP.filter(item => item.filename.trim() !== '');    
    if (listP.length > 0) {        
        if (window.onHintPlaylistStart) window.onHintPlaylistStart();         
        playAudioList(listP, true, 3); // true = looping; 3 = shuffle after 3 repetitions of the list
    } else {
        console.log('There are no files to play.');
    }
}



window.onHintPlaylistStart = function() {
    const btn = document.getElementById('btnHintLoop');
    if (btn) btn.classList.add('active');
};
window.onHintPlaylistCancel = function() {
    const btn = document.getElementById('btnHintLoop');
    if (btn) btn.classList.remove('active');
    const btns = document.querySelectorAll(".hintblock .btnHints");    
    for (let i = 0; i < btns.length; i++) {
        const btn = btns[i];
        btns[i].classList.remove("playAttention");
        //void btn.offsetWidth; // for redrawing
    }
};
window.onHintPlaylistAttention = function(idA) {
    // select the recording being played
    const btns = document.querySelectorAll(".hintblock .btnHints");    
    for (let i = 0; i < btns.length; i++) {
        const btn = btns[i];
        btn.classList.remove("errtrans");
        btn.classList.remove("truetrans");                
        if(btn.dataset.idwt !="" && btn.dataset.idwt == idA) {            
            btn.classList.add("playAttention");      
            const word = btn.dataset.word;
            const trans = btn.dataset.trans;            
            btn.innerHTML = `<b>${trans}</b><br>${word}`;
        } 
        else {
            btn.classList.remove("playAttention");     
        }
        //void btn.offsetWidth; // for redrawing
    }
};




window.cd = null;
window.cd = new window.CardDesign("20251128_"+`{{text:Speak->Learn}}`);

if( cd ) {
    setcheckboxAll(); 
    
    // FOR: HintButtons
    let lm = window.cd.getPar("HintQueueLimit");
    let items = window.cd.getPar("HintQueueItems"); 
    if( typeof lm !== "undefined" && typeof items !== "undefined" ) {
        window.hintStore = null;
        window.hintStore = new window.HintQueue( Number(lm) );    
        if (Array.isArray(items)) {        
            hintStore.items = JSON.parse(JSON.stringify(items));
        }
        else {
            hintStore.items = [];
        }
    }
    else {
        window.hintStore = null;
        hintStore = new window.HintQueue(10);    
    }    
    let word_Speak = `{{text:Speak}}`;
    let word_Learn = `{{text:Learn}}`;
    let fn_word_Speak = `{{text:FileName_Audio_Speak}}`; 
    let fn_word_Learn = `{{text:FileName_Audio_Learn}}`;
    addNewHint(word_Speak, word_Learn, fn_word_Speak, fn_word_Learn);
    window.cd.setPar("HintQueueLimit", hintStore.limit);
    window.cd.setPar("HintQueueItems", hintStore.items);
      
       
    // FOR: answer sound 
    if(window.cd.platform == "ankiweb") {
        if (checkedCheckboxAS) {
            playAudioList([        
            {filename: '{{text:FileName_Audio_Learn}}', speed: 1.0}
            ]);
        }
    }   
}

// ======================= MAIN ============================
</script> 



<script> // ***** 251210 <audio> with the standard button ********
// depends: CardDesign class, audio list player  
// === for «ankiweb»! ===
// === replacing the display <audio> with the standard button view ===
(function() {
    if(window.cd.platform == "ankiweb") {
        // Find all tags <audio>
        let audios = document.querySelectorAll("audio");
        audios.forEach(function(audio) {          
            if (audio.getAttribute("controls") !== "") return;
    
            // Let's check what's inside <source>
            let srcEl = audio.querySelector("source");
            if (!srcEl) return;
    
            let src = srcEl.getAttribute("src");
            if (!src) return;
            
            
            // We check to make sure we don't insert the button again.
            if (audio.nextElementSibling && audio.nextElementSibling.classList.contains("replay-button")) {
                return;
            }
                
            let a = document.createElement("a");
            a.className = "replay-button soundLink";            
            a.setAttribute("onclick", "stopAllAudio(); setTimeout(() => { playAudioSWeb('" + src + "', 1) }, 50); return false;");
            a.setAttribute("draggable", "false");
            
            a.innerHTML = `            
                <svg class="playImage" viewBox="0 0 64 64" version="1.1">
                    <circle cx="32" cy="32" r="29"></circle>
                    <path d="M56.502,32.301l-37.502,20.101l0.329,-40.804l37.173,20.703Z"></path>                    
                </svg>
            `;    
            
            audio.insertAdjacentElement("afterend", a);
            audio.style.display = "none";
            if (!audio.paused) {
                audio.pause();
            }
            audio.parentNode.removeChild(audio); // audio.remove();
        });    
    }
})();
// ================
// ***** 251210 <audio> with the standard button ********
</script> 

<script>
elstatusSL = document.getElementById('statusSL');
if(elstatusSL) elstatusSL.innerHTML = `{{text:Speak->Learn}}`.replace('->', '−>');
elS = document.getElementById('id_wordS');
elL = document.getElementById('id_wordL');
if(elS && elL) {
    speakLearn = `{{text:Speak->Learn}}`; // "EM->RU" — English USA->Russian
    const [SpeakLn, LearnLn] = speakLearn.split('->');  
    if(SpeakLn == 'AR') elS.classList.add('AR');
    if(LearnLn == 'AR') elL.classList.add('AR');    
}
</script>

""",            
            'afmt': """
<div class="allTrans" style="display: none;"></div>
<span style="display: none">{{Audio_Learn}}</span>

<div><div id="statusSL" style="position: absolute; font-size: 12px; color: #aaaaaaaa; top: 5px; left: 1px; z-index: 1019;"></div>
<!-- 
Specify a list of possible languages: AR, BG, DE, EM (USA), EN, ES, FR, IT, JA, KO, PL, PX (Brazil), RO, RU, TR, UK, ZH (China)
 -->
<div class="divAllTrans">
    <button id="btnHintBackLoop" onclick="playAllHintBackLoop(event)" class="btnHintsLoop" style="display: none;">🔊&nbsp;🔁</button>
    <button onclick="window.scrollTo(0, 0); allTranslations('EM,RO,UK,RU,PL,BG,IT,ES,PX,FR,DE,TR,AR,KO,JA,ZH',3)">L3</button>
    <button onclick="window.scrollTo(0, 0); allTranslations('EM,RU,UK,PL,BG,RO,IT,ES,PX,FR,DE,TR,AR,KO,JA,ZH')">L</button>
</div>
<span onclick="stopAllAudio(); reDraw('id_wordS', 'showWordSlowly');">{{Audio_Speak}}</span></div>
<div>

{{#Speak_Note}}
<span class="note">( {{Speak_Note}} )<span>
<br>
{{/Speak_Note}}
<span class="word_speak bgCard" style="--ws-delay: 0s; --ws-bcolor: var(--parbgCard); --ws-duration: 1s;" id="id_wordS">{{Speak}}</span>
</div>

<hr id=answer> <!-- do not delete -->

<div>
    <div class="inFrame bgYellow">        
        <span id="id_wordL" class="bgYellow word_learned showWordSlowly" style="--ws-delay: 0s; --ws-bcolor: var(--parYellow); --ws-duration: 1.5s;">{{Learn}}</span>
    </div>
</div>

{{#Learn_Note}}
<span class="note">( {{Learn_Note}} )<span>
<br>
{{/Learn_Note}}

<div class="psound">
<div>
    <a class="replay-buttonMy" id="id_slow1"
        onclick="stopAllAudio(); reDraw('id_wordL', 'showWordSlowly'); playAudioSWeb('{{text:FileName_Audio_Learn}}', 0.6);">
        <svg class="playImageMy" viewBox="0 0 64 64" version="1.1">
            <circle cx="32" cy="32" r="29" />
            <path d="M56.502,32.301l-37.502,20.101l0.329,-40.804l37.173,20.703Z" />
            <rect x="27" y="30" width="12" height="4" fill="lightgray" />
        </svg>
    </a>     
</div>
&nbsp;&nbsp;&nbsp;
<!-- drop-down menu --> 
<div class="dropdown"> 
  <button onclick="fDropDown()" class="dropbtn">•••</button>
  <div id="myDropdown" class="dropdown-content"></div>
</div>
&nbsp;&nbsp;&nbsp;
<div onclick="stopAllAudio(); reDraw('id_wordL', 'showWordSlowly');">{{Audio_Learn}}</div>
</div>

<div>
<span onclick="reDraw('id_wordL', 'showWordSlowly');
    playAudioList([
    {filename: '{{text:FileName_Audio_Learn}}', speed: 0.6},    
    {filename: '{{text:FileName_Audio_Speak}}', speed: 1.0},
    {filename: '{{text:FileName_Audio_Learn}}', speed: 1.0},
]);" style="cursor: pointer; z-index: 2000;"> {{#Image}}{{Image}}{{/Image}} </span>
</div>

{{#Note}}
<div>
<details>
  <summary style="color: aaaaaaaa;">note:</summary>
  {{hint:Note}}
</details>
</div>
{{/Note}}

<div style="position: fixed; font-size: 12px; color: #aaaaaaaa; bottom: 1px; left: 1px; z-index: 10000;" >{{Card}}</div>
<div style="position: fixed; font-size: 12px; color: #aaaaaaaa; bottom: 1px; left: 50%; transform: translateX(-50%); z-index: 10000;" >id: {{ID-number}}</div>
<div style="position: fixed; font-size: 12px; color: #aaaaaaaa; bottom: 1px; right: 1px; z-index: 10000;" >{{Category}}</div>



<script> // ***** 251210 reDraw ****************************
// redraws by removing and adding the class again
function reDraw(idel, classname) {
    let el = document.getElementById(idel);
    if(!el) return;    
    el.classList.remove(classname);
    void el.offsetWidth; // for redrawing
    el.classList.add(classname);  
}
// ***** 251210 reDraw ****************************
</script> 




<script> // ***** 251210 audio list player *****************
// === Audio file player ===
// === both individually and as a list ===
window.onHintPlaylistStart = null;
window.onHintPlaylistCancel = null;
window.onHintPlaylistAttention = null;
if(window.audioSWebManager) stopAllAudio();
// Global Audio Manager
if (!window.audioSWebManager) {
    window.audioSWebManager = {        
        audio: null, // Current player
        playlist: [], // Play queue
        currentIndex: 0,
        playlistId: 0, // Playlist ID for tracking relevance
        isPlaying: false,
        loop: false,
        shuffleN: 0, // after how many cycles will the mixture be mixed
        loopN: 0, // current cycle number
                
        initAudio() {
            if (!this.audio) {
                this.audio = new Audio();                
                // Audio event handlers
                this.audio.addEventListener('ended', () => {
                    this.onAudioEnded();
                });                
                this.audio.addEventListener('error', (e) => {
                    console.log('Audio error:', e);
                    this.onAudioEnded();
                });
            }
            return this.audio;
        },
        
        // Normal playback of a single file (cancels the playlist)
        playSingle(filename, speed = 1.0) {            
            this.stop();
            this.playFile(filename, speed); // Play the file
        },
        
        // Playing a file
        playFile(filename, speed = 1.0) {
            if (!filename || filename.trim() === '') return false;
            
            const audio = this.initAudio();  
            audio.pause();
            audio.currentTime = 0;
            audio.src = filename;
            audio.playbackRate = speed;
            
            // Attempting to reproduce
            return audio.play().then(() => {
                this.isPlaying = true;
                return true;
            }).catch(error => {
                console.log('Audio play failed:', error);
                this.isPlaying = false;
                return false;
            });
        },
        
        // Playing a playlist
        playPlaylist(files, loop = false, shuffleN = 0) {          
            this.playlistId++; // Increase the playlist ID to track relevance
            const currentPlaylistId = this.playlistId;            
            this.playlist = files; // Array of objects {filename, speed}
            this.currentIndex = 0;
            this.loop = loop;
            this.shuffleN = shuffleN;
            this.loopN = 0;
            this.isPlaying = true;    
        
            // We start playing the first file
            this.playNextInPlaylist(currentPlaylistId);
        },
        
        // shuffle file blocks
        shuffleBlocks(playlist) {
            // We divide it into blocks and immediately determine which blocks are empty.
            const blocks = [];
            let currentBlock = [];
            let currentBlockHasRealFiles = false;            
            for (let i = 0; i < playlist.length; i++) {
                const item = playlist[i];                
                if (item.filename === ':0') {                    
                    currentBlock.push(item); // Add end of block marker                   
                    // Save a block with information about whether it contains real files
                    blocks.push({
                        items: currentBlock,
                        hasRealFiles: currentBlockHasRealFiles
                    });                    
                    // Reset for the next block
                    currentBlock = [];
                    currentBlockHasRealFiles = false;
                } else {
                    currentBlock.push(item);
                    // Check if the file is real (not a service file)
                    if (!item.filename.startsWith(':')) {
                        currentBlockHasRealFiles = true;
                    }
                }
            }
            
            // Process the last block, if there is one
            if (currentBlock.length > 0) {
                blocks.push({
                    items: currentBlock,
                    hasRealFiles: currentBlockHasRealFiles
                });
            }
            
            // Split into non-empty and empty blocks
            const nonEmptyBlocks = blocks.filter(block => block.hasRealFiles);
            const emptyBlocks = blocks.filter(block => !block.hasRealFiles);
            
            // Shuffle only non-empty blocks if there is more than one
            if (nonEmptyBlocks.length > 1) {                
                for (let i = nonEmptyBlocks.length - 1; i > 0; i--) {
                    const j = Math.floor(Math.random() * (i + 1));
                    [nonEmptyBlocks[i], nonEmptyBlocks[j]] = [nonEmptyBlocks[j], nonEmptyBlocks[i]];
                }
            }
            
            // We collect the results
            const result = [];            
            // Adding shuffled non-empty blocks
            nonEmptyBlocks.forEach(block => {
                result.push(...block.items);
            });            
            // Add empty blocks at the end (usually this is just the final marker)
            emptyBlocks.forEach(block => {
                result.push(...block.items);
            });            
            return result;
        },
        
        
        // Play the next file in the playlist
        playNextInPlaylist(playlistId) {
            // Let's check if this playlist is still relevant
            if (playlistId !== this.playlistId) {
                console.log('Playlist outdated, stopping');
                return;
            }
            
            // Testing the boundaries
            if (this.currentIndex >= this.playlist.length) {
                if (this.loop) {
                    this.currentIndex = 0; // Looping
                    this.loopN += 1;
                    if(this.shuffleN > 0 && this.loopN >= this.shuffleN ) {
                        this.loopN = 0; 
                        this.playlist = this.shuffleBlocks(this.playlist);
                        this.shuffleN = 1;
                        console.log("The playlist blocks are shuffled and will change with each playback.");            
                    }
                } else {
                    this.isPlaying = false;
                    return; // End of playlist
                }
            }
            
            const item = this.playlist[this.currentIndex];
            
            if (item.filename.startsWith('!')) {                
                if (playlistId === this.playlistId) {
                    if (window.onHintPlaylistAttention) window.onHintPlaylistAttention(item.filename.slice(1)); 
                    this.currentIndex++;
                    this.playNextInPlaylist(playlistId);
                }
                return;                
            }
                
            // Checking the pause (file starts with :)
            if (item.filename.startsWith(':')) {
                const delay = parseInt(item.filename.substring(1));
                // end of block file mark (for shuffling)
                // {filename: ':0', speed: 1.0}                 
                if( delay != 0 ) {
                    setTimeout(() => {
                        // Checking that the playlist is still up to date
                        if (playlistId === this.playlistId) {
                            this.currentIndex++;
                            this.playNextInPlaylist(playlistId);
                        }
                    }, delay);
                }                    
                else {
                    if (playlistId === this.playlistId) {
                        this.currentIndex++;
                        this.playNextInPlaylist(playlistId);
                    }
                }
                return;
            }
            
            // Playing a regular file
            this.playFile(item.filename, item.speed || 1.0).then(success => {
                if (success) {
                    // currentIndex will increase after the end of the track (in onAudioEnded)
                } else {
                    // If there is a playback error, move on to the next one
                    if (playlistId === this.playlistId) {
                        this.currentIndex++;
                        this.playNextInPlaylist(playlistId);
                    }
                }
            });
        },
        
        // End of track handler
        onAudioEnded() {
            this.isPlaying = false;
            
            // If there is an active playlist
            if (this.playlist.length > 0 && this.playlistId > 0) {
                this.currentIndex++;
                this.playNextInPlaylist(this.playlistId);
            }
        },
       
        pause() {
            if (this.audio) {
                this.audio.pause();
                this.isPlaying = false;
            }
        },
                
        resume() {
            if (this.audio && !this.isPlaying && this.audio.currentTime > 0) {
                this.audio.play().then(() => {
                    this.isPlaying = true;
                }).catch(console.error);
            }
        },
                
        stop() {
            if (this.audio) {
                this.audio.pause();
                this.audio.currentTime = 0;
                this.audio.src = '';
            }
            
            this.playlist = [];
            this.playlistId = 0;
            this.currentIndex = 0;
            this.isPlaying = false;
        },
        
        // Skip the current track in the playlist
        skip() {
            if (this.playlist.length > 0) {
                if (this.audio) {
                    this.audio.pause();
                    this.audio.currentTime = 0;
                }
                this.currentIndex++;
                this.playNextInPlaylist(this.playlistId);
            }
        },
                
        getStatus() {
            return {
                isPlaying: this.isPlaying,
                playlistId: this.playlistId,
                currentIndex: this.currentIndex,
                playlistLength: this.playlist.length,
                currentTime: this.audio ? this.audio.currentTime : 0,
                duration: this.audio ? this.audio.duration : 0
            };
        }
    };
}



function playAudioSWeb(filename, speed) {
    if (!filename || filename.trim() === "") return;   
    if (window.onHintPlaylistCancel) window.onHintPlaylistCancel(); 
    // Using the manager for single playback
    window.audioSWebManager.playSingle(filename, speed || 1.0);
}

// Function for playing a list of files
function playAudioList(files, loop = false, shuffleN = 0) {    
    /* files - array of objects or strings: ['file1.mp3', 'file2.mp3']
    или
      [
        {filename: '!nameForAttention', speed: 1.0}, // call to the "window.onHintPlaylistAttention" function
        {filename: 'file1.mp3', speed: 1.0},
        {filename: ':1000', speed: 1.0}, // pause 1 second
        {filename: 'file2.mp3', speed: 1.5},
        {filename: ':0', speed: 1.0} // end of block file mark (for shuffling)
      ] 
    shuffleN - after how many cycles will the mixture be mixed    
    */        
    // Normalize the input data
    const normalizedFiles = files.map(item => {
        if (typeof item === 'string') {
            return { filename: item, speed: 1.0 };
        }
        return item;
    });    
    window.audioSWebManager.playPlaylist(normalizedFiles, loop, shuffleN);
}

function stopAllAudio() {
    window.audioSWebManager.stop();
}

function pauseAudio() {
    window.audioSWebManager.pause();
}

function resumeAudio() {
    window.audioSWebManager.resume();
}

// Skip the current track
function skipAudio() {
    window.audioSWebManager.skip();
}

function getAudioStatus() {
    return window.audioSWebManager.getStatus();
}
// ================
// ***** 251210 audio list player *****************
</script>


<script> // ***** 251210 CardDesign class ******************
/* =================== CardDesign class =================== */
if (!window.CardDesign) {
window.CardDesign = class {
    constructor(cd_id) {
        this.id = cd_id;        
        this.version = "1.0";
        this.platform = this.detectAnkiPlatform();
        this.dataPar = {}; // Parameters for all currently viewed cards       
        this.data = {}; // Data entered on the face of the card        
        this.loadPar(); // Load parameters for all currently viewed cards    
        if(this.isAnswer())
            this.load();
        else
            this.save(); // clear as empty
 
        this.boundSave = this.save.bind(this);
        window.addEventListener("beforeunload", this.boundSave);       
        this.boundSaveIsHidden = this.saveIsHidden.bind(this);
        document.addEventListener("visibilitychange", this.boundSaveIsHidden);
        
        // hide elements not for this platform
        this.hideElementsPlatform();
    }
    
    
    destroy() {        
        window.removeEventListener("beforeunload", this.boundSave);
        document.removeEventListener("visibilitychange", this.boundSaveIsHidden);
    }
    
    isAnswer() {
        let el = document.getElementById("answer");
        if(el) {            
            return true;            
        }        
        return false;        
    }
    
    detectAnkiPlatform() {
        if (typeof pycmd !== "undefined") return "desk";
        if (typeof AnkiDroidJS !== "undefined") return "ankidroid";
        if (document.getElementById("qa_box")) return "ankiweb";
        return "ios";
    }
    
    save() {       
        try {            
            window.localStorage.setItem(
                "CardDesign_" + this.id,
                JSON.stringify({
                    data: this.data       
                })
            );
        } catch (e) {
            console.log("CardDesign.save error:", e);
        }
    }
    
    saveIsHidden() {
        if (document.hidden) this.save();    
    }

    load() {
        try {            
            const saved = window.localStorage.getItem("CardDesign_" + this.id);
            if (!saved) return;
            const obj = JSON.parse(saved);
            if (obj.data) this.data = obj.data;
        } catch (e) {
            console.log("CardDesign.load error:", e);
        }
    }
    
    savePar() {       
        try {
            window.localStorage.setItem(
                "CardDesign_Par_" + this.id,
                JSON.stringify({
                    data: this.dataPar     
                })
            );
        } catch (e) {
            console.log("CardDesign.savePar error:", e);
        }
    }

    loadPar() {
        try {
            const saved = window.localStorage.getItem("CardDesign_Par_" + this.id);
            if (!saved) return;
            const obj = JSON.parse(saved);
            if (obj.data) this.dataPar = obj.data;
        } catch (e) {
            console.log("CardDesign.loadPar error:", e);
        }
    }

    log(msg) {
        console.log(`[CardDesign v=${this.version}, app=${this.platform}] ${msg}`);
    }
    
    showAnswer() {
        if (this.platform == "desk") {            
            pycmd("ans");
        }
        else if (this.platform == "ankidroid") {
            window.showAnswer();
        }
        else if (this.platform == "ankiweb") {
            const btn = document.querySelector("#ansarea .btn");            
            if (btn) btn.click();
            else this.log("ERROR: Button not found in showAnswer()");
        }
    }    
    

    setData(key, value) {
        this.data[key] = value;
        this.save();
    }

    getData(key) {
        return this.data[key];
    }
    
    setPar(key, value) {
        this.dataPar[key] = value;
        this.savePar();
    }

    getPar(key) {
        return this.dataPar[key];
    }
    
    // hide elements not for this app or party
    hideElementsPlatform() {
        let Elements = null;
        if( this.platform == "desk") {
            Elements = document.getElementsByClassName('hideindesk');            
            for (let elem of Elements) elem.style= "display: none";                            
        }
        else if( this.platform == "ankidroid") {
            Elements = document.getElementsByClassName('hideinankidroid');
            for (let elem of Elements) elem.style= "display: none";
        }        
        else if( this.platform == "ankiweb") {
            Elements = document.getElementsByClassName('hideinankiweb');
            for (let elem of Elements) elem.style= "display: none";            
        }
        else if( this.platform == "ios") {
            Elements = document.getElementsByClassName('hideinios');
            for (let elem of Elements) elem.style= "display: none";            
        }
        
        if(this.isAnswer()) {
            Elements = document.getElementsByClassName('hideisback');
            for (let elem of Elements) elem.style= "display: none";            
        }
        else {            
            Elements = document.getElementsByClassName('hideisfront');
            for (let elem of Elements) elem.style= "display: none";            
        }
    }    
}}
/* ========↑↑↑======== CardDesign class ========↑↑↑======== */
// ***** 251210 CardDesign class ******************
</script> 



<script> // ======================= MAIN ============================

window.cd = null;
window.cd = new window.CardDesign("20251128_"+`{{text:Speak->Learn}}`);
if( cd ) {
    // FOR: answer sound 
    if(window.cd.platform == "ankiweb") {  
        if (checkedCheckboxAS) {      
            playAudioList([        
            {filename: '{{text:FileName_Audio_Learn}}', speed: 0.7},
            {filename: '{{text:FileName_Audio_Speak}}', speed: 1.0},
            {filename: '{{text:FileName_Audio_Learn}}', speed: 1.0}
            ]);
        }
    }    
}


// ======================= MAIN ============================
</script> 



<script> // ***** 251210 drop-down menu ********************

/* ---- COPY ---- */
// Copy to clipboard for older browsers
function fallbackCopyToClipboard(text) {
  const textArea = document.createElement("textarea");
  textArea.value = text;
  textArea.style.position = "fixed"; // To prevent page scrolling
  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();    
  try {
    document.execCommand('copy');    
  } catch (err) {
    console.error('Clipboard write error: ', err);
  }  
  document.body.removeChild(textArea);
}

// The main function of copying to the clipboard
async function  copyToClipboard(text) {    
    if(window.cd.platform == "desk") {
        try {
            // An alternative method for older browsers           
            fallbackCopyToClipboard(text);            
        } catch(e) {
            await navigator.clipboard.writeText(text);            
        }   
    }
    else {
        try {
            await navigator.clipboard.writeText(text);
        } catch(e) {
            // An alternative method for older browsers           
            fallbackCopyToClipboard(text);
        }        
    }        
}
/* ^^^^ COPY ^^^^ */

if (!window.languageData) {
window.languageData = [
    { code: "AR", name: "العربية", codeGoogle: "ar", youglishName: "arabic" },
    { code: "DE", name: "Deutsch", codeGoogle: "de", youglishName: "german" },
    { code: "EM", name: "English US", codeGoogle: "en", youglishName: "" },
    { code: "EN", name: "English UK", codeGoogle: "en", youglishName: "" },
    { code: "ES", name: "español", codeGoogle: "es", youglishName: "spanish" },
    { code: "FR", name: "français", codeGoogle: "fr", youglishName: "french" },
    { code: "IT", name: "italiano", codeGoogle: "it", youglishName: "italian" },
    { code: "JA", name: "日本語", codeGoogle: "ja", youglishName: "japanese" },
    { code: "PT", name: "português PT", codeGoogle: "pt-PT", youglishName: "portuguese" },
    { code: "PX", name: "português BR", codeGoogle: "pt-BR", youglishName: "portuguese" },
    { code: "ZH", name: "中文", codeGoogle: "zh", youglishName: "chinese" },
    { code: "AD", name: "адыгабзэ", codeGoogle: "ady", youglishName: "" },
    { code: "AF", name: "Afrikaans", codeGoogle: "af", youglishName: "" },
    { code: "AM", name: "አማርኛ", codeGoogle: "am", youglishName: "" },
    { code: "BE", name: "беларуская", codeGoogle: "be", youglishName: "" },
    { code: "BG", name: "български", codeGoogle: "bg", youglishName: "" },
    { code: "BN", name: "বাংলা", codeGoogle: "bn", youglishName: "" },
    { code: "BS", name: "bosanski", codeGoogle: "bs", youglishName: "" },
    { code: "CA", name: "català", codeGoogle: "ca", youglishName: "" },
    { code: "CS", name: "čeština", codeGoogle: "cs", youglishName: "" },
    { code: "DA", name: "dansk", codeGoogle: "da", youglishName: "" },
    { code: "EL", name: "ελληνικά", codeGoogle: "el", youglishName: "greek" },
    { code: "EO", name: "esperanto", codeGoogle: "eo", youglishName: "" },
    { code: "ET", name: "eesti", codeGoogle: "et", youglishName: "" },
    { code: "FA", name: "فارسی", codeGoogle: "fa", youglishName: "persian" },
    { code: "FI", name: "suomi", codeGoogle: "fi", youglishName: "" },
    { code: "HE", name: "עברית", codeGoogle: "he", youglishName: "hebrew" },
    { code: "HI", name: "हिन्दी", codeGoogle: "hi", youglishName: "hindi" },
    { code: "HR", name: "hrvatski", codeGoogle: "hr", youglishName: "" },
    { code: "HU", name: "magyar", codeGoogle: "hu", youglishName: "" },
    { code: "HY", name: "հայերեն", codeGoogle: "hy", youglishName: "" },
    { code: "ID", name: "bahasa Indonesia", codeGoogle: "id", youglishName: "" },
    { code: "KA", name: "ქართული", codeGoogle: "ka", youglishName: "" },
    { code: "KK", name: "қазақша", codeGoogle: "kk", youglishName: "" },
    { code: "KN", name: "ಕನ್ನಡ", codeGoogle: "kn", youglishName: "" },
    { code: "KO", name: "한국어", codeGoogle: "ko", youglishName: "korean" },
    { code: "LT", name: "lietuvių", codeGoogle: "lt", youglishName: "" },
    { code: "LV", name: "latviešu", codeGoogle: "lv", youglishName: "" },
    { code: "MK", name: "македонски", codeGoogle: "mk", youglishName: "" },
    { code: "MR", name: "मराठी", codeGoogle: "mr", youglishName: "" },
    { code: "NL", name: "Nederlands", codeGoogle: "nl", youglishName: "dutch" },
    { code: "NN", name: "nynorsk", codeGoogle: "nn", youglishName: "" },
    { code: "NO", name: "norsk", codeGoogle: "no", youglishName: "" },
    { code: "PA", name: "ਪੰਜਾਬੀ", codeGoogle: "pa", youglishName: "" },
    { code: "PL", name: "polski", codeGoogle: "pl", youglishName: "polish" },
    { code: "RO", name: "română", codeGoogle: "ro", youglishName: "romanian" },
    { code: "RU", name: "русский", codeGoogle: "ru", youglishName: "russian" },
    { code: "SK", name: "slovenčina", codeGoogle: "sk", youglishName: "" },
    { code: "SL", name: "slovenščina", codeGoogle: "sl", youglishName: "" },
    { code: "SQ", name: "Shqip", codeGoogle: "sq", youglishName: "" },
    { code: "SR", name: "српски", codeGoogle: "sr", youglishName: "" },
    { code: "SV", name: "svenska", codeGoogle: "sv", youglishName: "swedish" },
    { code: "TA", name: "தமிழ்", codeGoogle: "ta", youglishName: "" },
    { code: "TE", name: "తెలుగు", codeGoogle: "te", youglishName: "" },
    { code: "TH", name: "ภาษาไทย", codeGoogle: "th", youglishName: "thai" },
    { code: "TI", name: "ትግርኛ", codeGoogle: "ti", youglishName: "" },
    { code: "TR", name: "Türkçe", codeGoogle: "tr", youglishName: "turkish" },
    { code: "UK", name: "українська", codeGoogle: "uk", youglishName: "ukrainian" },
    { code: "UR", name: "اردو", codeGoogle: "ur", youglishName: "" },
    { code: "VI", name: "Tiếng Việt", codeGoogle: "vi", youglishName: "vietnamese" }
];
}

// request for AI to clipboard
function getForII(txt, Speak, Learn) {
    
    function findNameByCode(code) {
        const upperCode = code.toUpperCase();
        const language = languageData.find(lang => lang.code === upperCode);        
        return language ? language.name : " ";
    }
    
    function findCodeGoogleByCode(code) {
        const upperCode = code.toUpperCase();
        const language = languageData.find(lang => lang.code === upperCode);        
        return language ? language.codeGoogle : " ";
    }
    
    let SpeakN = findCodeGoogleByCode(Speak);
    let LearnN = findCodeGoogleByCode(Learn);
    SpeakN = SpeakN + " (" + findNameByCode(Speak) + ")"; 
    LearnN = LearnN + " (" + findNameByCode(Learn) + ")";  
    
    retTxt = `This text is written in English.
I speak the language: ${SpeakN} (country code or language name) well.
I started learning the language: ${LearnN} (country code or language name)
There is a text in the language I am learning: ${txt}
Repeat this text in your answer on a separate line.
On a separate line below, provide a translation of this text into: ${SpeakN}
On another separate line, provide an example of its use (preferably a simple, uncomplicated sentence).
On the line below, provide a translation of the example (indicated on the line above) into: ${SpeakN}
On another line below, describe the rules in this text. Perhaps you can share some specific details about this text (taking into account the language I know well), so that it would be useful for those just beginning to learn this language.
When you give an answer, you don't need any additional words, like this is a translation, and this is an example, except for the last line where you describe the rules, where you can use different words for clarification`;       
  
  copyToClipboard(retTxt);
}


/* When the user clicks the button,
toggle between hiding and showing the drop-down content */
function fDropDown() {
  navigator.vibrate(30); // vibration when pressed   
  document.getElementById("myDropdown").classList.toggle("show");
  var urlEl, yourLink, word = `{{text:Learn}}`;

  urlEl = document.getElementById("urlII");
  yourLink = "javascript:void(0);";
  urlEl.setAttribute('href', yourLink);
  speakLearn = `{{text:Speak->Learn}}`; // "EM->RU" — English USA->Russian
  const [SpeakLn, LearnLn] = speakLearn.split('->');    
  urlEl.onclick = function() {
      getForII(word, SpeakLn, LearnLn);      
  }; 
  
  function getLanguageByCode(code) {
    return languageData.find(lang => lang.code === code.toUpperCase());
  }  

  const speakLang = getLanguageByCode(SpeakLn);
  const learnLang = getLanguageByCode(LearnLn);
  
  const speakCodeLower = speakLang.codeGoogle;
  const learnCodeLower = learnLang.codeGoogle;
  
    
  urlEl = document.getElementById("urlFORVO");
  yourLink = "https://forvo.com/search/" + encodeURIComponent(word) + "/" + learnCodeLower + "/";
  urlEl.setAttribute('href', yourLink);
  
  urlEl = document.getElementById("urlYOUGLISH");  
  yourLink = "https://youglish.com/pronounce/" + encodeURIComponent(word) + "/" + learnLang.youglishName + "?";
  urlEl.setAttribute('href', yourLink);
  
  urlEl = document.getElementById("urlGOOGLE");
  yourLink = "https://translate.google.com/?hl=" + speakCodeLower + 
             "&sl=" + learnCodeLower + 
             "&tl=" + speakCodeLower + 
             "&text=" + encodeURIComponent(word);
  urlEl.setAttribute('href', yourLink);
    
  urlEl = document.getElementById("urlYANDEX"); 
  yourLink = "https://translate.yandex.ru/?source_lang=" + learnCodeLower + 
             "&target_lang=" + speakCodeLower + 
             "&text=" + encodeURIComponent(word);
  urlEl.setAttribute('href', yourLink);
  
  urlEl = document.getElementById("urlWORDREF"); 
  yourLink = "https://www.wordreference.com/" + learnCodeLower + speakCodeLower
    + "/" + encodeURIComponent(word);
  urlEl.setAttribute('href', yourLink);
  
} 


elmyDropdown = document.getElementById("myDropdown");
if(elmyDropdown) {
    elmyDropdown.innerHTML =
        `<a id="urlII" href="#">FOR AI? (to the clipboard)</a>`    
        + `<a id="urlFORVO" href="#">FORVO (voice)</a>`        
        + `<a id="urlYOUGLISH" href="#">YOUGLISH (video subtitles)</a>`        
        + `<a id="urlGOOGLE" href="#">GOOGLE (translation)</a>`
        + `<a id="urlYANDEX" href="#">YANDEX (translation)</a>`
        + `<a id="urlWORDREF" href="#">WORDREF (translation)</a>`;
}


// Close a drop-down menu if the user clicks outside of it
if(!window.f_wonclick) {
    window.f_wonclick = true;
    window.onclick = function(event) {
      if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
          }
        }
      }
    }
}
    


// ***** 251210 drop-down menu ********************
</script>


<script> // ***** 251210 <audio> with the standard button ********
// depends: CardDesign class, audio list player  
// === for «ankiweb»! ===
// === replacing the display <audio> with the standard button view ===
(function() {
    if(window.cd.platform == "ankiweb") {
        // Find all tags <audio>
        let audios = document.querySelectorAll("audio");
        audios.forEach(function(audio) {          
            if (audio.getAttribute("controls") !== "") return;
    
            // Let's check what's inside <source>
            let srcEl = audio.querySelector("source");
            if (!srcEl) return;
    
            let src = srcEl.getAttribute("src");
            if (!src) return;
            
            
            // We check to make sure we don't insert the button again.
            if (audio.nextElementSibling && audio.nextElementSibling.classList.contains("replay-button")) {
                return;
            }
                
            let a = document.createElement("a");
            a.className = "replay-button soundLink";            
            a.setAttribute("onclick", "stopAllAudio(); setTimeout(() => { playAudioSWeb('" + src + "', 1) }, 50); return false;");
            a.setAttribute("draggable", "false");
            
            a.innerHTML = `            
                <svg class="playImage" viewBox="0 0 64 64" version="1.1">
                    <circle cx="32" cy="32" r="29"></circle>
                    <path d="M56.502,32.301l-37.502,20.101l0.329,-40.804l37.173,20.703Z"></path>                    
                </svg>
            `;    
            
            audio.insertAdjacentElement("afterend", a);
            audio.style.display = "none";
            if (!audio.paused) {
                audio.pause();
            }
            audio.parentNode.removeChild(audio); // audio.remove();
        });    
    }
})();
// ================
// ***** 251210 <audio> with the standard button ********
</script> 



<script> // ***** 251210 show all languages *****************
// gets all data for the index
async function lookupWordAllLangs(index = '') {   
    try {
        // Download once and cache
        if (!window._vocabCache) {
            const response = await fetch("_book2_note_p.json");
            window._vocabCache = await response.json();
        }
        
        // Get all languages ​​for a given index
        const allLangsData = window._vocabCache?.[index];
        if (allLangsData) {
            return allLangsData; //  {en: {...}, ru: {...}, ...}
        }
        return null;
    } catch (error) {
        console.error('ERROR:', error);
        return null;
    }
}

// Function to get a specific language (if needed)
async function lookupWord(index = '', lang = '') {
    const allLangs = await lookupWordAllLangs(index);
    if (allLangs && allLangs[lang]) {
        return { word: allLangs[lang].w, note: allLangs[lang].p };
    }
    return null;
}


function allTranslations(listLn = '', cntLn = 0) {
    // Checking if the container is displayed
    const container = document.querySelector('.allTrans');    
    let btnHBLoop = document.getElementById("btnHintBackLoop");
    // If the container is visible and was opened with this button, hide it and exit.   
    if (container.style.display !== 'none' && container.dataset.cntlnstr == String(cntLn)) {
        container.style.display = 'none';     
        if(btnHBLoop) btnHBLoop.style.display = 'none'; 
        container.classList.remove('translation-active');
        // Remove the active class from all elements
        document.querySelectorAll('.translation-item.active').forEach(el => {
            el.classList.remove('active');
        });
        delete container.dataset.cntlnstr;
        return;
    }
    
    container.dataset.cntlnstr = String(cntLn);
    
    // We receive data
    let index = `{{text:ID-number}}`;
    let speakLearn = `{{text:Speak->Learn}}`;
    let [SpeakLn, LearnLn] = speakLearn.split('->');
    
    // Getting a list of languages ​​to display
    let languages = listLn.split(',').filter(lang => 
        lang.trim() !== ''
        /* && lang !== SpeakLn
        && lang !== LearnLn */
    );
    
    // If cntLn > 0, limit the quantity (except SpeakLn and LearnLn)
    if (cntLn > 0) {
        languages = languages.slice(0, cntLn);
    }
    
    // If there are no languages ​​to display, exit.
    if (languages.length === 0) {
        console.log('There are no languages ​​to display.');
        return;
    }
        
    lookupWordAllLangs(index).then(allLanguagesData => {
        if (!allLanguagesData) {
            console.log(`Data for index ${index} not found`);
            return;
        }
        
        // Generating HTML
        let html = '';
        
        // We go through the required languages
        languages.forEach(lang => {
            const entry = allLanguagesData[lang];
            if (entry) {
                const langName = getLangName(lang);
                const soundName = 'book2_phr_N' + index + '_' + lang + '.mp3';
                const idwt = entry.w + "#" + lang; 
                html += `
                <div class="translation-item" data-lang="${lang}"  data-word="${entry.w}" data-fnword="${soundName}" data-idwt="${idwt}" onclick="playTranslationSound('${index}', '${lang}', this)">
                    <div class="language-label">${langName.toLowerCase()}:&nbsp;</div><div class="translation-item-word">`;
                
                if (entry.p && entry.p.trim() !== "") {
                    html += `${entry.w} (${entry.p})`;
                } else {
                    html += `${entry.w}`;
                }
                
                html += `</div></div>`;
            }
        });
        
        container.innerHTML = html;                
        container.style.display = 'inline-block';
        btnHBLoop.style.display = 'inline-block';
        container.classList.add('translation-active');
        
    }).catch(error => {
        console.error('Error loading translations:', error);
    });
}


// play all the prompts in a loop
function playAllHintBackLoop(event) {
    let elB = event.target;
    if(elB.classList.contains("active")) {
        elB.classList.remove('active');
        if (window.onHintPlaylistCancel) window.onHintPlaylistCancel();
        stopAllAudio();
        return;
    }
    const btns = document.querySelectorAll(".allTrans .translation-item");
    let listP = [];    
    for (let i = 0; i < btns.length; i++) {
        const btn = btns[i];
        if(btn.dataset.word && btn.dataset.word.trim() !== "") {
            // Adding files to the list
            listP.push(
                {filename: '!'+String(btn.dataset.idwt), speed: 1.0}, // call to the "window.onHintPlaylistAttention" function                
                {filename: btn.dataset.fnword || '', speed: 1.0},
                {filename: ':1000', speed: 1.0}, // pause 1 second
                {filename: ':0', speed: 1.0}// end of block file mark (for shuffling)
            );
        }
    }
    
    // Filter empty files (just in case)
    listP = listP.filter(item => item.filename.trim() !== '');    
    if (listP.length > 0) {        
        if (window.onHintPlaylistStart) window.onHintPlaylistStart();         
        playAudioList(listP, true, 0); // true = looping; 3 = shuffle after 3 repetitions of the list
    } else {
        console.log('There are no files to play.');
    }
}


window.onHintPlaylistStart = function() {
    const btn = document.getElementById('btnHintBackLoop');
    if (btn) btn.classList.add('active');
};

window.onHintPlaylistCancel = function() {
    const btn = document.getElementById('btnHintBackLoop');
    if (btn) btn.classList.remove('active');    
};

window.onHintPlaylistAttention = function(idA) {
    // select the recording being played
    const btns = document.querySelectorAll(".allTrans .translation-item");    
    for (let i = 0; i < btns.length; i++) {
        const btn = btns[i];                
        if(btn.dataset.idwt !="" && btn.dataset.idwt == idA) {                
            btn.classList.add("active");             
        } 
        else {
            btn.classList.remove("active");
        }
        //void btn.offsetWidth; // for redrawing
    }
};



// Function to play a sound when clicking on a translation
function playTranslationSound(index, lang, element) {    
    stopAllAudio();  
    // Remove the active class from all elements
    document.querySelectorAll('.translation-item.active').forEach(el => {
        el.classList.remove('active');
    });
    element.classList.add('active');
    const soundName = 'book2_phr_N' + index + '_' + lang + '.mp3';      
    playAudioSWeb(soundName, 1);
}

function getLangName(code) {
    const langNames = {
        'AR': 'ar', 'BG': 'bg', 'DE': 'de', 'EM': 'en',
        'EN': 'en', 'ES': 'es', 'FR': 'fr', 'IT': 'it',
        'JA': 'ja', 'KO': 'ko', 'PL': 'pl', 'PX': 'pt-br',
        'RO': 'ro', 'RU': 'ru', 'TR': 'tr', 'UK': 'uk',
        'ZH': 'zh'
    };
    return langNames[code] || code.toLowerCase();
}

// ***** 251210 show all languages *****************
</script>


<script>
elstatusSL = document.getElementById('statusSL');
if(elstatusSL) elstatusSL.innerHTML = `{{text:Speak->Learn}}`.replace('->', '−>');
elS = document.getElementById('id_wordS');
elL = document.getElementById('id_wordL');
if(elS && elL) {
    speakLearn = `{{text:Speak->Learn}}`; // "EM->RU" — English USA->Russian
    const [SpeakLn, LearnLn] = speakLearn.split('->');  
    if(SpeakLn == 'AR') elS.classList.add('AR');
    if(LearnLn == 'AR') elL.classList.add('AR');    
}
</script>

""",
        },
        {
            'name': 'Card 2',
            'qfmt': """
<div id="statusSL" style="position: absolute; font-size: 12px; color: #aaaaaaaa; top: 1px; left: 1px; z-index: 1019;" ></div>
<div onclick="stopAllAudio(); reDraw('id_wordS', 'showWordSlowly');">{{Audio_Speak}}</div>

<div>
{{#Speak_Note}}
<span class="note">( {{Speak_Note}} )<span>
<br>
{{/Speak_Note}}

<span class="word_speak bgCard" style="--ws-delay: 0s; --ws-bcolor: var(--parbgCard); --ws-duration: 1s;" id="id_wordS">{{Speak}}</span>
</div>

<div id="fLearn" style="display: none;">{{text:Learn}}</div>
<div id="input_id1" contenteditable="true" class="editable" oninput="isGoodInput('fLearn', 'input_id1');" autocomplete="off" spellcheck="false" onkeydown="inputKD(event);"></div>
<span style="font-size: 0.6em;">(type text or speak it)</span>
</p>

<label style="font-size: 14px;" title="Hint from the past 10 cards" class="chBox">
  <input type="checkbox" id="checkboxH10" name="hintPast10" value="yes" onchange="checkboxH10CH(event);"> hint past 10
</label>

<label style="font-size: 14px;" class="chBox hideinankidroid hideindesk hideinios" title="For Ankiweb: Play the sound of the word being studied when you press the 'Show Answer' button">
  <input type="checkbox" id="checkboxAS" name="ankiweb sound" value="yes" onchange="checkboxASCH(event);" class="hideinankidroid hideindesk hideinios"> answer sound
</label>
<label style="font-size: 14px;" class="chBox hideinankidroid">
  <input type="checkbox" id="checkboxAF" name="autofocusInput" value="yes" onchange="checkboxAFCH('input_id1', event);" class="hideinankidroid"> autofocus
</label>
&nbsp;&nbsp;
<button onclick="ClearInputId('input_id1')" class="btnClear" title="Clear the input field" style="border-radius: 7px;">CLR</button>
&nbsp;&nbsp;
<button onclick="Suggest1('fLearn', 'input_id1')" class="btnSug" title="Suggest 1 character" style="border-radius: 7px;">&nbsp;?&nbsp;</button>

<div class="hintblock" id="hintblock1" style="display: none;">
<div class="spbtnHints">
<button id="btnHint1" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHint2" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHint3" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHint4" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHint5" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHint6" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHint7" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHint8" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHint9" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHint10" class="btnHints">&nbsp;</button>
</div>
<div class="spbtnHints">
<button id="btnHintLoop" onclick="playAllHintLoop(event)" class="btnHintsLoop">&nbsp;🔊&nbsp;🔁&nbsp;</button>
</div>
</div>

<div style="position: fixed; font-size: 12px; color: #aaaaaaaa; bottom: 1px; left: 1px; z-index: 10000;" >{{Card}}</div>
<div style="position: fixed; font-size: 12px; color: #aaaaaaaa; bottom: 1px; left: 50%; transform: translateX(-50%); z-index: 10000;" >id: {{ID-number}}</div>
<div style="position: fixed; font-size: 12px; color: #aaaaaaaa; bottom: 1px; right: 1px; z-index: 10000;" >{{Category}}</div>


<script> // ***** 251210 reDraw ****************************
// redraws by removing and adding the class again
function reDraw(idel, classname) {
    let el = document.getElementById(idel);
    if(!el) return;    
    el.classList.remove(classname);
    void el.offsetWidth; // for redrawing
    el.classList.add(classname);  
}
// ***** 251210 reDraw ****************************
</script> 


<script> // ***** 251210 audio list player *****************
// === Audio file player ===
// === both individually and as a list ===
window.onHintPlaylistStart = null;
window.onHintPlaylistCancel = null;
window.onHintPlaylistAttention = null;
if(window.audioSWebManager) stopAllAudio();
// Global Audio Manager
if (!window.audioSWebManager) {
    window.audioSWebManager = {        
        audio: null, // Current player
        playlist: [], // Play queue
        currentIndex: 0,
        playlistId: 0, // Playlist ID for tracking relevance
        isPlaying: false,
        loop: false,
        shuffleN: 0, // after how many cycles will the mixture be mixed
        loopN: 0, // current cycle number
                
        initAudio() {
            if (!this.audio) {
                this.audio = new Audio();                
                // Audio event handlers
                this.audio.addEventListener('ended', () => {
                    this.onAudioEnded();
                });                
                this.audio.addEventListener('error', (e) => {
                    console.log('Audio error:', e);
                    this.onAudioEnded();
                });
            }
            return this.audio;
        },
        
        // Normal playback of a single file (cancels the playlist)
        playSingle(filename, speed = 1.0) {            
            this.stop();
            this.playFile(filename, speed); // Play the file
        },
        
        // Playing a file
        playFile(filename, speed = 1.0) {
            if (!filename || filename.trim() === '') return false;
            
            const audio = this.initAudio();  
            audio.pause();
            audio.currentTime = 0;
            audio.src = filename;
            audio.playbackRate = speed;
            
            // Attempting to reproduce
            return audio.play().then(() => {
                this.isPlaying = true;
                return true;
            }).catch(error => {
                console.log('Audio play failed:', error);
                this.isPlaying = false;
                return false;
            });
        },
        
        // Playing a playlist
        playPlaylist(files, loop = false, shuffleN = 0) {          
            this.playlistId++; // Increase the playlist ID to track relevance
            const currentPlaylistId = this.playlistId;            
            this.playlist = files; // Array of objects {filename, speed}
            this.currentIndex = 0;
            this.loop = loop;
            this.shuffleN = shuffleN;
            this.loopN = 0;
            this.isPlaying = true;    
        
            // We start playing the first file
            this.playNextInPlaylist(currentPlaylistId);
        },
        
        // shuffle file blocks
        shuffleBlocks(playlist) {
            // We divide it into blocks and immediately determine which blocks are empty.
            const blocks = [];
            let currentBlock = [];
            let currentBlockHasRealFiles = false;            
            for (let i = 0; i < playlist.length; i++) {
                const item = playlist[i];                
                if (item.filename === ':0') {                    
                    currentBlock.push(item); // Add end of block marker                   
                    // Save a block with information about whether it contains real files
                    blocks.push({
                        items: currentBlock,
                        hasRealFiles: currentBlockHasRealFiles
                    });                    
                    // Reset for the next block
                    currentBlock = [];
                    currentBlockHasRealFiles = false;
                } else {
                    currentBlock.push(item);
                    // Check if the file is real (not a service file)
                    if (!item.filename.startsWith(':')) {
                        currentBlockHasRealFiles = true;
                    }
                }
            }
            
            // Process the last block, if there is one
            if (currentBlock.length > 0) {
                blocks.push({
                    items: currentBlock,
                    hasRealFiles: currentBlockHasRealFiles
                });
            }
            
            // Split into non-empty and empty blocks
            const nonEmptyBlocks = blocks.filter(block => block.hasRealFiles);
            const emptyBlocks = blocks.filter(block => !block.hasRealFiles);
            
            // Shuffle only non-empty blocks if there is more than one
            if (nonEmptyBlocks.length > 1) {                
                for (let i = nonEmptyBlocks.length - 1; i > 0; i--) {
                    const j = Math.floor(Math.random() * (i + 1));
                    [nonEmptyBlocks[i], nonEmptyBlocks[j]] = [nonEmptyBlocks[j], nonEmptyBlocks[i]];
                }
            }
            
            // We collect the results
            const result = [];            
            // Adding shuffled non-empty blocks
            nonEmptyBlocks.forEach(block => {
                result.push(...block.items);
            });            
            // Add empty blocks at the end (usually this is just the final marker)
            emptyBlocks.forEach(block => {
                result.push(...block.items);
            });            
            return result;
        },
        
        
        // Play the next file in the playlist
        playNextInPlaylist(playlistId) {
            // Let's check if this playlist is still relevant
            if (playlistId !== this.playlistId) {
                console.log('Playlist outdated, stopping');
                return;
            }
            
            // Testing the boundaries
            if (this.currentIndex >= this.playlist.length) {
                if (this.loop) {
                    this.currentIndex = 0; // Looping
                    this.loopN += 1;
                    if(this.shuffleN > 0 && this.loopN >= this.shuffleN ) {
                        this.loopN = 0; 
                        this.playlist = this.shuffleBlocks(this.playlist);
                        this.shuffleN = 1;
                        console.log("The playlist blocks are shuffled and will change with each playback.");            
                    }
                } else {
                    this.isPlaying = false;
                    return; // End of playlist
                }
            }
            
            const item = this.playlist[this.currentIndex];
            
            if (item.filename.startsWith('!')) {                
                if (playlistId === this.playlistId) {
                    if (window.onHintPlaylistAttention) window.onHintPlaylistAttention(item.filename.slice(1)); 
                    this.currentIndex++;
                    this.playNextInPlaylist(playlistId);
                }
                return;                
            }
                
            // Checking the pause (file starts with :)
            if (item.filename.startsWith(':')) {
                const delay = parseInt(item.filename.substring(1));
                // end of block file mark (for shuffling)
                // {filename: ':0', speed: 1.0}                 
                if( delay != 0 ) {
                    setTimeout(() => {
                        // Checking that the playlist is still up to date
                        if (playlistId === this.playlistId) {
                            this.currentIndex++;
                            this.playNextInPlaylist(playlistId);
                        }
                    }, delay);
                }                    
                else {
                    if (playlistId === this.playlistId) {
                        this.currentIndex++;
                        this.playNextInPlaylist(playlistId);
                    }
                }
                return;
            }
            
            // Playing a regular file
            this.playFile(item.filename, item.speed || 1.0).then(success => {
                if (success) {
                    // currentIndex will increase after the end of the track (in onAudioEnded)
                } else {
                    // If there is a playback error, move on to the next one
                    if (playlistId === this.playlistId) {
                        this.currentIndex++;
                        this.playNextInPlaylist(playlistId);
                    }
                }
            });
        },
        
        // End of track handler
        onAudioEnded() {
            this.isPlaying = false;
            
            // If there is an active playlist
            if (this.playlist.length > 0 && this.playlistId > 0) {
                this.currentIndex++;
                this.playNextInPlaylist(this.playlistId);
            }
        },
       
        pause() {
            if (this.audio) {
                this.audio.pause();
                this.isPlaying = false;
            }
        },
                
        resume() {
            if (this.audio && !this.isPlaying && this.audio.currentTime > 0) {
                this.audio.play().then(() => {
                    this.isPlaying = true;
                }).catch(console.error);
            }
        },
                
        stop() {
            if (this.audio) {
                this.audio.pause();
                this.audio.currentTime = 0;
                this.audio.src = '';
            }
            
            this.playlist = [];
            this.playlistId = 0;
            this.currentIndex = 0;
            this.isPlaying = false;
        },
        
        // Skip the current track in the playlist
        skip() {
            if (this.playlist.length > 0) {
                if (this.audio) {
                    this.audio.pause();
                    this.audio.currentTime = 0;
                }
                this.currentIndex++;
                this.playNextInPlaylist(this.playlistId);
            }
        },
                
        getStatus() {
            return {
                isPlaying: this.isPlaying,
                playlistId: this.playlistId,
                currentIndex: this.currentIndex,
                playlistLength: this.playlist.length,
                currentTime: this.audio ? this.audio.currentTime : 0,
                duration: this.audio ? this.audio.duration : 0
            };
        }
    };
}



function playAudioSWeb(filename, speed) {
    if (!filename || filename.trim() === "") return;   
    if (window.onHintPlaylistCancel) window.onHintPlaylistCancel(); 
    // Using the manager for single playback
    window.audioSWebManager.playSingle(filename, speed || 1.0);
}

// Function for playing a list of files
function playAudioList(files, loop = false, shuffleN = 0) {    
    /* files - array of objects or strings: ['file1.mp3', 'file2.mp3']
    или
      [
        {filename: '!nameForAttention', speed: 1.0}, // call to the "window.onHintPlaylistAttention" function
        {filename: 'file1.mp3', speed: 1.0},
        {filename: ':1000', speed: 1.0}, // pause 1 second
        {filename: 'file2.mp3', speed: 1.5},
        {filename: ':0', speed: 1.0} // end of block file mark (for shuffling)
      ] 
    shuffleN - after how many cycles will the mixture be mixed    
    */        
    // Normalize the input data
    const normalizedFiles = files.map(item => {
        if (typeof item === 'string') {
            return { filename: item, speed: 1.0 };
        }
        return item;
    });    
    window.audioSWebManager.playPlaylist(normalizedFiles, loop, shuffleN);
}

function stopAllAudio() {
    window.audioSWebManager.stop();
}

function pauseAudio() {
    window.audioSWebManager.pause();
}

function resumeAudio() {
    window.audioSWebManager.resume();
}

// Skip the current track
function skipAudio() {
    window.audioSWebManager.skip();
}

function getAudioStatus() {
    return window.audioSWebManager.getStatus();
}
// ================
// ***** 251210 audio list player *****************
</script> 



<script> // ***** 251210 CardDesign class ******************
/* =================== CardDesign class =================== */
if (!window.CardDesign) {
window.CardDesign = class {
    constructor(cd_id) {
        this.id = cd_id;        
        this.version = "1.0";
        this.platform = this.detectAnkiPlatform();
        this.dataPar = {}; // Parameters for all currently viewed cards       
        this.data = {}; // Data entered on the face of the card        
        this.loadPar(); // Load parameters for all currently viewed cards    
        if(this.isAnswer())
            this.load();
        else
            this.save(); // clear as empty
 
        this.boundSave = this.save.bind(this);
        window.addEventListener("beforeunload", this.boundSave);       
        this.boundSaveIsHidden = this.saveIsHidden.bind(this);
        document.addEventListener("visibilitychange", this.boundSaveIsHidden);
        
        // hide elements not for this platform
        this.hideElementsPlatform();
    }
    
    
    destroy() {        
        window.removeEventListener("beforeunload", this.boundSave);
        document.removeEventListener("visibilitychange", this.boundSaveIsHidden);
    }
    
    isAnswer() {
        let el = document.getElementById("answer");
        if(el) {            
            return true;            
        }        
        return false;        
    }
    
    detectAnkiPlatform() {
        if (typeof pycmd !== "undefined") return "desk";
        if (typeof AnkiDroidJS !== "undefined") return "ankidroid";
        if (document.getElementById("qa_box")) return "ankiweb";
        return "ios";
    }
    
    save() {       
        try {            
            window.localStorage.setItem(
                "CardDesign_" + this.id,
                JSON.stringify({
                    data: this.data       
                })
            );
        } catch (e) {
            console.log("CardDesign.save error:", e);
        }
    }
    
    saveIsHidden() {
        if (document.hidden) this.save();    
    }

    load() {
        try {            
            const saved = window.localStorage.getItem("CardDesign_" + this.id);
            if (!saved) return;
            const obj = JSON.parse(saved);
            if (obj.data) this.data = obj.data;
        } catch (e) {
            console.log("CardDesign.load error:", e);
        }
    }
    
    savePar() {       
        try {
            window.localStorage.setItem(
                "CardDesign_Par_" + this.id,
                JSON.stringify({
                    data: this.dataPar     
                })
            );
        } catch (e) {
            console.log("CardDesign.savePar error:", e);
        }
    }

    loadPar() {
        try {
            const saved = window.localStorage.getItem("CardDesign_Par_" + this.id);
            if (!saved) return;
            const obj = JSON.parse(saved);
            if (obj.data) this.dataPar = obj.data;
        } catch (e) {
            console.log("CardDesign.loadPar error:", e);
        }
    }

    log(msg) {
        console.log(`[CardDesign v=${this.version}, app=${this.platform}] ${msg}`);
    }
    
    showAnswer() {
        if (this.platform == "desk") {            
            pycmd("ans");
        }
        else if (this.platform == "ankidroid") {
            window.showAnswer();
        }
        else if (this.platform == "ankiweb") {
            const btn = document.querySelector("#ansarea .btn");            
            if (btn) btn.click();
            else this.log("ERROR: Button not found in showAnswer()");
        }
    }    
    

    setData(key, value) {
        this.data[key] = value;
        this.save();
    }

    getData(key) {
        return this.data[key];
    }
    
    setPar(key, value) {
        this.dataPar[key] = value;
        this.savePar();
    }

    getPar(key) {
        return this.dataPar[key];
    }
    
    // hide elements not for this app or party
    hideElementsPlatform() {
        let Elements = null;
        if( this.platform == "desk") {
            Elements = document.getElementsByClassName('hideindesk');            
            for (let elem of Elements) elem.style= "display: none";                            
        }
        else if( this.platform == "ankidroid") {
            Elements = document.getElementsByClassName('hideinankidroid');
            for (let elem of Elements) elem.style= "display: none";
        }        
        else if( this.platform == "ankiweb") {
            Elements = document.getElementsByClassName('hideinankiweb');
            for (let elem of Elements) elem.style= "display: none";            
        }
        else if( this.platform == "ios") {
            Elements = document.getElementsByClassName('hideinios');
            for (let elem of Elements) elem.style= "display: none";            
        }
        
        if(this.isAnswer()) {
            Elements = document.getElementsByClassName('hideisback');
            for (let elem of Elements) elem.style= "display: none";            
        }
        else {            
            Elements = document.getElementsByClassName('hideisfront');
            for (let elem of Elements) elem.style= "display: none";            
        }
    }    
}}
/* ========↑↑↑======== CardDesign class ========↑↑↑======== */
// ***** 251210 CardDesign class ******************
</script> 


<script> // ***** 251210 HintQueue class *******************
/* =================== HintQueue class =================== */
if (!window.HintQueue) {
window.HintQueue = class {
    constructor(limit = 10) {
        this.limit = limit;
        this.items = []; // [{word: "...", trans: "...", fnword: "...", fntrans: "..."}]
    }

    add(word, trans, fnword, fntrans) {
        if (!word) return;    
        // We delete the duplicate if there is one.
        this.items = this.items.filter(item =>
            !(item.word === word && item.trans === trans)
        );    
        // Add to the end
        this.items.push({ word, trans, fnword, fntrans });    
        // Limiting the queue size
        if (this.items.length > this.limit) {
            this.items.shift();
        }
    }

    get(i) {
        if (i < 0 || i >= this.items.length) return ["", ""];
        const { word, trans, fnword, fntrans } = this.items[i];
        return [word, trans, fnword, fntrans];
    }

    size() {
        return this.items.length;
    }

    /* Returns a NEW array of shuffled pairs */
    getShuffled() {
        const arr = [...this.items];
        for (let i = arr.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        return arr;
    }
}}
/* ========↑↑↑======== HintQueue class ========↑↑↑======== */
// ***** 251210 HintQueue class *******************
</script> 


<script> // ======================= MAIN ============================

// play all the prompts in a loop
function playAllHintLoop(event) {
    let elB = event.target;
    if(elB.classList.contains("active")) {
        elB.classList.remove('active');
        if (window.onHintPlaylistCancel) window.onHintPlaylistCancel();
        stopAllAudio();
        return;
    }
    const btns = document.querySelectorAll(".hintblock .btnHints");
    let listP = [];
    
    for (let i = 0; i < btns.length; i++) {
        const btn = btns[i];
        if(btn.dataset.trans && btn.dataset.trans.trim() !== "") {
            // Adding files to the list
            listP.push(
                {filename: '!'+String(btn.dataset.idwt), speed: 1.0}, // call to the "window.onHintPlaylistAttention" function
                {filename: btn.dataset.fntrans || '', speed: 1.0},
                {filename: btn.dataset.fnword || '', speed: 1.0},
                {filename: ':1000', speed: 1.0}, // pause 1 second
                {filename: ':0', speed: 1.0}// end of block file mark (for shuffling)
            );
        }
    }
    
    // Filter empty files (just in case)
    listP = listP.filter(item => item.filename.trim() !== '');    
    if (listP.length > 0) {        
        if (window.onHintPlaylistStart) window.onHintPlaylistStart();         
        playAudioList(listP, true, 3); // true = looping; 3 = shuffle after 3 repetitions of the list
    } else {
        console.log('There are no files to play.');
    }
}


window.onHintPlaylistStart = function() {
    const btn = document.getElementById('btnHintLoop');
    if (btn) btn.classList.add('active');
};
window.onHintPlaylistCancel = function() {
    const btn = document.getElementById('btnHintLoop');
    if (btn) btn.classList.remove('active');
    const btns = document.querySelectorAll(".hintblock .btnHints");    
    for (let i = 0; i < btns.length; i++) {
        const btn = btns[i];
        btns[i].classList.remove("playAttention");
        //void btn.offsetWidth; // for redrawing
    }
};
window.onHintPlaylistAttention = function(idA) {
    // select the recording being played
    const btns = document.querySelectorAll(".hintblock .btnHints");    
    for (let i = 0; i < btns.length; i++) {
        const btn = btns[i];
        btn.classList.remove("errtrans");
        btn.classList.remove("truetrans");                
        if(btn.dataset.idwt !="" && btn.dataset.idwt == idA) {                
            btn.classList.add("playAttention"); 
            const word = btn.dataset.word;
            const trans = btn.dataset.trans;            
            btn.innerHTML = `<b>${trans}</b><br>${word}`;
        } 
        else {
            btn.classList.remove("playAttention");     
        }
        //void btn.offsetWidth; // for redrawing
    }
};

checkedCheckboxH10 = false;
function checkboxH10CH(event){     
    let ch = event.target.checked; 
    checkedCheckboxH10 = ch;    
    let elH10 = document.getElementById("hintblock1");
    if(checkedCheckboxH10) {
        if(elH10) elH10.style.display = "flex";   
    }
    else {
        if(elH10) elH10.style.display = "none";    
    }    
    window.cd.setPar("checkboxH10"+`{{Card}}`, String(ch)); 
    fillHintButtons();   
}


checkedCheckboxAS = false;
function checkboxASCH(event){     
    let ch = event.target.checked; 
    checkedCheckboxAS = ch;    
    window.cd.setPar("checkboxAS", String(ch));    
}


checkedCheckboxAF = false;
function checkboxAFCH(id, event){         
    let el = document.getElementById("input_id1");
    let ch = event.target.checked;     
    checkedCheckboxAF = ch;        
    window.cd.setPar("checkboxAF", String(ch));  
    if( ch ) {
        setTimeout(function() {                    
            moveCursorToEnd(el);
        }, 100);    
    }        
}



function inputKD(event) {
    if (event.key === "Enter") {        
        event.preventDefault(); // cancel the standard behavior        
        if(window.cd) {                                        
            window.cd.showAnswer();
            if(window.cd.platform == "ankiweb") {                
                playWebSoundFront();
            }
        } 
    }
    else if (event.key === "?") {
        event.preventDefault(); // cancel the standard behavior
        Suggest1('fLearn', 'input_id1');
    }
}


function onlySimpleText(str) {     
    /// Convert to plain text
    // Romanian substitutions
    str = str.replace(/[Ș]/gu, "Ş");
    str = str.replace(/[ș]/gu, "ş");
    str = str.replace(/[Ț]/gu, "Ţ");
    str = str.replace(/[ț]/gu, "ţ");
    // Russian replacements
    str = str.replace(/[ё]/gu, "е");
    str = str.replace(/[Ё]/gu, "Е");
    str = str.replace(/[ӂ]/gu, "ж");
    str = str.replace(/[Ӂ]/gu, "Ж");
    // Remove HTML tags
    str = str.replace(/<[^>]*>/g, "");
    // Remove Unicode punctuation (apostrophes, quotation marks, periods, commas, brackets, dashes, etc.)
    str = str.replace(/\p{P}+/gu, " ");
    // Remove other "symbols" like ©, ™, § — Symbol category
    str = str.replace(/\p{S}+/gu, " ");
    str = str.replace(/​/gu, "");
    // Normalize spaces
    str = str.replace(/\s+/g, " ");
    return str.toLowerCase().trim();
}


function isGoodInput(idField, idInput) {
    ///     
    let el1 = document.getElementById(idField);
    let el2 = document.getElementById(idInput);
    let str1 = "";
    let str2 = "";
    if(el1 && el2){
        str1 = el1.textContent;
        str1 = onlySimpleText(str1);
        str2 = el2.innerText;            
        str2 = onlySimpleText(str2);
        if(str1 === str2 || str1+" "+str1 === str2 || str1+" "+str1+" "+str1 === str2 || str1+" "+str1+" "+str1+" "+str1 === str2 || str1+" "+str1+" "+str1+" "+str1+" " + str1 == str2) {
            el2.classList.remove("colorInput");
            el2.classList.remove("ErrorInput");
            if( !el2.classList.contains("goodInput")) {
                el2.classList.add("goodInput"); // el2.style.color = "green";  
                if(window.cd) window.cd.setData("inpHTMLClass", "goodInput"); 
                playAudioSWeb(`{{text:FileName_Audio_Learn}}`, 1);
            }
                
        }    
        else if(str1.indexOf(str2)==0 || str2.indexOf(str1+" ")==0) {
            el2.classList.remove("goodInput");
            el2.classList.remove("ErrorInput");
            el2.classList.add("colorInput"); // el2.style.color = "#00aeff";
            if(window.cd) window.cd.setData("inpHTMLClass", "colorInput"); 
        }        
        else {
            el2.classList.remove("colorInput");
            el2.classList.remove("goodInput");
            el2.classList.add("ErrorInput"); // el2.style.color = "red";     
            if(window.cd) window.cd.setData("inpHTMLClass", "ErrorInput");    
        }        
    }     
    
    if(window.cd) window.cd.setData("inpHTML", el2.innerHTML);
}


function ClearInputId(id) {
    /// clear text in Input
    let el = document.getElementById(id);
    if(el) {
        el.innerHTML = "";
        if(window.cd) window.cd.setData("inpHTML", "");
        if(window.cd) window.cd.setData("inpHTMLClass", "colorInput");
        el.focus();
    }       
}



function moveCursorToEnd(el) {
    el.focus(); // focus required
    const range = document.createRange();
    const sel = window.getSelection();
    // take the last child node
    const lastNode = el.lastChild;
    if (lastNode) {
        if (lastNode.nodeType === Node.TEXT_NODE) {
            // if it's a text node, place the cursor at the end of the text
            range.setStart(lastNode, lastNode.textContent.length);
        } else {
            // if it's an element (for example, span), put it after it
            range.setStartAfter(lastNode);
        }
        range.collapse(true);
        sel.removeAllRanges();
        sel.addRange(range);
    }
}

function Suggest1(idField, idInput) {
    let el1 = document.getElementById(idField);
    let el2 = document.getElementById(idInput);
    if (!el1 || !el2) return;

    let str1 = onlySimpleText(el1.innerText);
    let str2 = onlySimpleText(el2.innerText);

    let n2 = str2.length;
    let n1 = str1.length;

    el2.focus();

    if (n2 < n1) {
        let nextChar = str1[n2];        
        if( nextChar==" " && el2.innerText.slice(-1) == ' ' ) {            
            while(n2+1 < n1 && nextChar==" ") {
                n2 += 1;
                nextChar = str1[n2];
            }
        }
        if (n2 < n1) {
            if( nextChar==" " ) el2.innerHTML += " ";
            else el2.innerHTML += `<span style="color: #ff00ff;">` + nextChar + `</span>​`;
        }
    }
    if(window.cd) window.cd.setData("inpHTML", el2.innerHTML);    
    moveCursorToEnd(el2);
    isGoodInput(idField, idInput);
}



function setcheckboxAll(){
    if(window.cd) {  
        try {
            let ch = window.cd.getPar("checkboxAF");
            let el = document.getElementById("checkboxAF");
            if(el) {
                if(ch == "true") {
                    el.checked = true; 
                    checkedCheckboxAF = true;                      
                    let elInp = document.getElementById("input_id1");
                    if(elInp)                    
                        setTimeout(function() {   
                            elInp.focus();
                        }, 500);
                }
                else{
                    el.checked = false;  
                    checkedCheckboxAF = false;
                }
                 
            } 
        }              
        catch(e) {}
        
        try {
            let ch = window.cd.getPar("checkboxAS");            
            let el = document.getElementById("checkboxAS");            
            if(el) {                                  
                if(ch == "true") {
                    el.checked = true;  
                    checkedCheckboxAS = true;                    
                }
                else {                    
                    el.checked = false; 
                    checkedCheckboxAS = false;                    
                }                    
            } 
        }
        catch(e) {}
        
        
        try {
            let ch = window.cd.getPar("checkboxH10"+`{{Card}}`);            
            let el = document.getElementById("checkboxH10");            
            if(el) {
                let elH10 = document.getElementById("hintblock1");
                if(ch == "true") {
                    el.checked = true;  
                    checkedCheckboxH10 = true;
                    if(elH10) elH10.style.display = "flex";
                }
                else {                    
                    el.checked = false; 
                    checkedCheckboxH10 = false;  
                    if(elH10) elH10.style.display = "none";                  
                }                    
            } 
        }
        catch(e) {}
    }
}





// === HintButtons ===
// Function of outputting words to buttons (after shuffling) 
function fillHintButtons() {
    const shuffled = hintStore.getShuffled();

    const btns = document.querySelectorAll(".hintblock .btnHints");

    for (let i = 0; i < btns.length; i++) {
        const btn = btns[i];

        if (i < shuffled.length) {
            btn.dataset.word = shuffled[i].word;
            btn.dataset.trans = shuffled[i].trans;
            btn.dataset.idwt = shuffled[i].word + "#" + shuffled[i].trans;
            btn.dataset.fnword = String(shuffled[i].fnword);
            btn.dataset.fntrans = String(shuffled[i].fntrans); 
            btn.innerHTML = shuffled[i].trans;             
        } else {
            // if really less than 10 words
            btn.dataset.word = "";
            btn.dataset.trans = "";
            btn.dataset.idwt = "";
            btn.dataset.fnword = "";
            btn.dataset.fntrans = "";
            btn.innerHTML = "";        
        }
        btn.classList.remove("errtrans");
        btn.classList.remove("truetrans");
    }
}

// adding a new word
function addNewHint(word_Speak, word_Learn, fn_word_Speak, fn_word_Learn) {
    hintStore.add(word_Speak, word_Learn, fn_word_Speak, fn_word_Learn);    
    fillHintButtons();
}

document.removeEventListener('click', window.clickHintButtons);
window.clickHintButtons = function (event) {
    const btn = event.target.closest(".btnHints");
    if (!btn) return;   

    const word = btn.dataset.word;
    const trans = btn.dataset.trans;
    const fnword = btn.dataset.fnword;    
    const fntrans = btn.dataset.fntrans;
    if (!word) return;

    // reveal the translation    
    btn.innerHTML = `<b>${trans}</b><br>${word}`;
    let word_Learn = `{{text:Learn}}`;
    // we check the correctness
    if (trans !== word_Learn) {   // variable of the current correct translation
        btn.classList.add("errtrans");
    }
    else {
        btn.classList.add("truetrans");  
        let el2 = document.getElementById("input_id1");          
        if(el2) {
            el2.innerHTML = trans;
            el2.classList.remove("goodInput");
            el2.classList.remove("ErrorInput");
            el2.classList.add("goodInput");
        }
    }
    
    // sound fntrans fnword
    if(fntrans != "") {
        try{
            if (window.onHintPlaylistCancel) window.onHintPlaylistCancel();
            playAudioList([fntrans, fnword]); 
        }
        catch(er){}
    } 
}
document.addEventListener('click', window.clickHintButtons);

// =====================


    
window.cd = null;
window.cd = new window.CardDesign("20251128_"+`{{text:Speak->Learn}}`);

if( cd ) {
    setcheckboxAll(); 
    
    // FOR: HintButtons
    let lm = window.cd.getPar("HintQueueLimit");
    let items = window.cd.getPar("HintQueueItems"); 
    if( typeof lm !== "undefined" && typeof items !== "undefined" ) {
        window.hintStore = null;
        window.hintStore = new window.HintQueue( Number(lm) );    
        if (Array.isArray(items)) {        
            hintStore.items = JSON.parse(JSON.stringify(items));
        }
        else {
            hintStore.items = [];
        }
    }
    else {
        window.hintStore = null;
        hintStore = new window.HintQueue(10);    
    }    
    let word_Speak = `{{text:Speak}}`;
    let word_Learn = `{{text:Learn}}`;
    let fn_word_Speak = `{{text:FileName_Audio_Speak}}`; 
    let fn_word_Learn = `{{text:FileName_Audio_Learn}}`;
    addNewHint(word_Speak, word_Learn, fn_word_Speak, fn_word_Learn);
    window.cd.setPar("HintQueueLimit", hintStore.limit);
    window.cd.setPar("HintQueueItems", hintStore.items);
      
   
    
    // FOR: answer sound 
    if(window.cd.platform == "ankiweb") {
        if (checkedCheckboxAS) {
            playAudioList([        
            {filename: '{{text:FileName_Audio_Speak}}', speed: 1.0}        
            ]);
        }   
    }   
}

// ======================= MAIN ============================
</script> 


<script> // ***** 251210 <audio> with the standard button ********
// depends: CardDesign class, audio list player  
// === for «ankiweb»! ===
// === replacing the display <audio> with the standard button view ===
(function() {
    if(window.cd.platform == "ankiweb") {
        // Find all tags <audio>
        let audios = document.querySelectorAll("audio");
        audios.forEach(function(audio) {          
            if (audio.getAttribute("controls") !== "") return;
    
            // Let's check what's inside <source>
            let srcEl = audio.querySelector("source");
            if (!srcEl) return;
    
            let src = srcEl.getAttribute("src");
            if (!src) return;
            
            
            // We check to make sure we don't insert the button again.
            if (audio.nextElementSibling && audio.nextElementSibling.classList.contains("replay-button")) {
                return;
            }
                
            let a = document.createElement("a");
            a.className = "replay-button soundLink";            
            a.setAttribute("onclick", "stopAllAudio(); setTimeout(() => { playAudioSWeb('" + src + "', 1) }, 50); return false;");
            a.setAttribute("draggable", "false");
            
            a.innerHTML = `            
                <svg class="playImage" viewBox="0 0 64 64" version="1.1">
                    <circle cx="32" cy="32" r="29"></circle>
                    <path d="M56.502,32.301l-37.502,20.101l0.329,-40.804l37.173,20.703Z"></path>                    
                </svg>
            `;    
            
            audio.insertAdjacentElement("afterend", a);
            audio.style.display = "none";
            if (!audio.paused) {
                audio.pause();
            }
            audio.parentNode.removeChild(audio); // audio.remove();
        });    
    }
})();
// ================
// ***** 251210 <audio> with the standard button ********
</script> 



<script>
elstatusSL = document.getElementById('statusSL');
if(elstatusSL) elstatusSL.innerHTML = `{{text:Speak->Learn}}`.replace('->', '−>');
elS = document.getElementById('id_wordS');
elL = document.getElementById('id_wordL');
if(elS && elL) {
    speakLearn = `{{text:Speak->Learn}}`; // "EM->RU" — English USA->Russian
    const [SpeakLn, LearnLn] = speakLearn.split('->');  
    if(SpeakLn == 'AR') elS.classList.add('AR');
    if(LearnLn == 'AR') elL.classList.add('AR');    
}
</script>

""",
            'afmt': """
<div class="allTrans" style="display: none;"></div>


<span style="display: none">{{Audio_Learn}}</span>

<div>
<div id="statusSL" style="position: absolute; font-size: 12px; color: #aaaaaaaa; top: 5px; left: 1px; z-index: 1019;"></div>
<!-- 
Specify a list of possible languages: AR, BG, DE, EM (USA), EN, ES, FR, IT, JA, KO, PL, PX (Brazil), RO, RU, TR, UK, ZH (China)
 -->
<div class="divAllTrans">
    <button id="btnHintBackLoop" onclick="playAllHintBackLoop(event)" class="btnHintsLoop" style="display: none;">🔊&nbsp;🔁</button>
    <button onclick="window.scrollTo(0, 0); allTranslations('EM,RO,UK,RU,PL,BG,IT,ES,PX,FR,DE,TR,AR,KO,JA,ZH',3)">L3</button>
    <button onclick="window.scrollTo(0, 0); allTranslations('EM,RU,UK,PL,BG,RO,IT,ES,PX,FR,DE,TR,AR,KO,JA,ZH')">L</button>    
</div>
<span onclick="stopAllAudio(); reDraw('id_wordS', 'showWordSlowly');" style="zoom: 1.0;">{{Audio_Speak}}</span></div>
<div>
{{#Speak_Note}}
<span class="note">( {{Speak_Note}} )<span>
<br>
{{/Speak_Note}}
<span class="word_speak bgCard" style="--ws-delay: 0s; --ws-bcolor: var(--parbgCard); --ws-duration: 1s;" id="id_wordS">{{Speak}}</span>
</div>

<p id="inpHTML" class="hideisfront">---</p>

<hr id=answer> <!-- do not delete -->

<div>
    <div class="inFrame bgYellow">        
        <span id="id_wordL" class="bgYellow word_learned showWordSlowly" style="--ws-delay: 0s; --ws-bcolor: var(--parYellow); --ws-duration: 1.5s;">{{Learn}}</span>
    </div>
</div>

{{#Learn_Note}}
<span class="note">( {{Learn_Note}} )<span>
<br>
{{/Learn_Note}}

<div class="psound">
<div>
    <a class="replay-buttonMy" id="id_slow1"
        onclick="stopAllAudio(); reDraw('id_wordL', 'showWordSlowly'); playAudioSWeb('{{text:FileName_Audio_Learn}}', 0.6);">
        <svg class="playImageMy" viewBox="0 0 64 64" version="1.1">
            <circle cx="32" cy="32" r="29" />
            <path d="M56.502,32.301l-37.502,20.101l0.329,-40.804l37.173,20.703Z" />
            <rect x="27" y="30" width="12" height="4" fill="lightgray" />
        </svg>
    </a>
</div>    
&nbsp;&nbsp;&nbsp;        
<!-- drop-down menu -->
<div class="dropdown" style="margin: 10px 0px;">  
  <button onclick="fDropDown()" class="dropbtn">•••</button>
  <div id="myDropdown" class="dropdown-content"></div>
</div>
&nbsp;&nbsp;&nbsp;
<div onclick="stopAllAudio(); reDraw('id_wordL', 'showWordSlowly');" style="zoom: 1.0;">{{Audio_Learn}}</div>
</div>

<div>
<span onclick="reDraw('id_wordL', 'showWordSlowly');
    playAudioList([
    {filename: '{{text:FileName_Audio_Learn}}', speed: 0.6},    
    {filename: '{{text:FileName_Audio_Speak}}', speed: 1.0},
    {filename: '{{text:FileName_Audio_Learn}}', speed: 1.0},
]);" style="cursor: pointer;"> {{#Image}}{{Image}}{{/Image}} </span>
</div>

{{#Note}}
<div>
<details>
  <summary style="color: aaaaaaaa;">note:</summary>
  {{hint:Note}}
</details>
</div>
{{/Note}}

<div style="position: fixed; font-size: 12px; color: #aaaaaaaa; bottom: 1px; left: 1px; z-index: 10000;" >{{Card}}</div>
<div style="position: fixed; font-size: 12px; color: #aaaaaaaa; bottom: 1px; left: 50%; transform: translateX(-50%); z-index: 10000;" >id: {{ID-number}}</div>
<div style="position: fixed; font-size: 12px; color: #aaaaaaaa; bottom: 1px; right: 1px; z-index: 10000;" >{{Category}}</div>

      
<script> // ***** 251210 reDraw ****************************
// redraws by removing and adding the class again
function reDraw(idel, classname) {
    let el = document.getElementById(idel);
    if(!el) return;    
    el.classList.remove(classname);
    void el.offsetWidth; // for redrawing
    el.classList.add(classname);  
}
// ***** 251210 reDraw ****************************
</script> 



<script> // ***** 251210 audio list player *****************
// === Audio file player ===
// === both individually and as a list ===
window.onHintPlaylistStart = null;
window.onHintPlaylistCancel = null;
window.onHintPlaylistAttention = null;
if(window.audioSWebManager) stopAllAudio();
// Global Audio Manager
if (!window.audioSWebManager) {
    window.audioSWebManager = {        
        audio: null, // Current player
        playlist: [], // Play queue
        currentIndex: 0,
        playlistId: 0, // Playlist ID for tracking relevance
        isPlaying: false,
        loop: false,
        shuffleN: 0, // after how many cycles will the mixture be mixed
        loopN: 0, // current cycle number
                
        initAudio() {
            if (!this.audio) {
                this.audio = new Audio();                
                // Audio event handlers
                this.audio.addEventListener('ended', () => {
                    this.onAudioEnded();
                });                
                this.audio.addEventListener('error', (e) => {
                    console.log('Audio error:', e);
                    this.onAudioEnded();
                });
            }
            return this.audio;
        },
        
        // Normal playback of a single file (cancels the playlist)
        playSingle(filename, speed = 1.0) {            
            this.stop();
            this.playFile(filename, speed); // Play the file
        },
        
        // Playing a file
        playFile(filename, speed = 1.0) {
            if (!filename || filename.trim() === '') return false;
            
            const audio = this.initAudio();  
            audio.pause();
            audio.currentTime = 0;
            audio.src = filename;
            audio.playbackRate = speed;
            
            // Attempting to reproduce
            return audio.play().then(() => {
                this.isPlaying = true;
                return true;
            }).catch(error => {
                console.log('Audio play failed:', error);
                this.isPlaying = false;
                return false;
            });
        },
        
        // Playing a playlist
        playPlaylist(files, loop = false, shuffleN = 0) {          
            this.playlistId++; // Increase the playlist ID to track relevance
            const currentPlaylistId = this.playlistId;            
            this.playlist = files; // Array of objects {filename, speed}
            this.currentIndex = 0;
            this.loop = loop;
            this.shuffleN = shuffleN;
            this.loopN = 0;
            this.isPlaying = true;    
        
            // We start playing the first file
            this.playNextInPlaylist(currentPlaylistId);
        },
        
        // shuffle file blocks
        shuffleBlocks(playlist) {
            // We divide it into blocks and immediately determine which blocks are empty.
            const blocks = [];
            let currentBlock = [];
            let currentBlockHasRealFiles = false;            
            for (let i = 0; i < playlist.length; i++) {
                const item = playlist[i];                
                if (item.filename === ':0') {                    
                    currentBlock.push(item); // Add end of block marker                   
                    // Save a block with information about whether it contains real files
                    blocks.push({
                        items: currentBlock,
                        hasRealFiles: currentBlockHasRealFiles
                    });                    
                    // Reset for the next block
                    currentBlock = [];
                    currentBlockHasRealFiles = false;
                } else {
                    currentBlock.push(item);
                    // Check if the file is real (not a service file)
                    if (!item.filename.startsWith(':')) {
                        currentBlockHasRealFiles = true;
                    }
                }
            }
            
            // Process the last block, if there is one
            if (currentBlock.length > 0) {
                blocks.push({
                    items: currentBlock,
                    hasRealFiles: currentBlockHasRealFiles
                });
            }
            
            // Split into non-empty and empty blocks
            const nonEmptyBlocks = blocks.filter(block => block.hasRealFiles);
            const emptyBlocks = blocks.filter(block => !block.hasRealFiles);
            
            // Shuffle only non-empty blocks if there is more than one
            if (nonEmptyBlocks.length > 1) {                
                for (let i = nonEmptyBlocks.length - 1; i > 0; i--) {
                    const j = Math.floor(Math.random() * (i + 1));
                    [nonEmptyBlocks[i], nonEmptyBlocks[j]] = [nonEmptyBlocks[j], nonEmptyBlocks[i]];
                }
            }
            
            // We collect the results
            const result = [];            
            // Adding shuffled non-empty blocks
            nonEmptyBlocks.forEach(block => {
                result.push(...block.items);
            });            
            // Add empty blocks at the end (usually this is just the final marker)
            emptyBlocks.forEach(block => {
                result.push(...block.items);
            });            
            return result;
        },
        
        
        // Play the next file in the playlist
        playNextInPlaylist(playlistId) {
            // Let's check if this playlist is still relevant
            if (playlistId !== this.playlistId) {
                console.log('Playlist outdated, stopping');
                return;
            }
            
            // Testing the boundaries
            if (this.currentIndex >= this.playlist.length) {
                if (this.loop) {
                    this.currentIndex = 0; // Looping
                    this.loopN += 1;
                    if(this.shuffleN > 0 && this.loopN >= this.shuffleN ) {
                        this.loopN = 0; 
                        this.playlist = this.shuffleBlocks(this.playlist);
                        this.shuffleN = 1;
                        console.log("The playlist blocks are shuffled and will change with each playback.");            
                    }
                } else {
                    this.isPlaying = false;
                    return; // End of playlist
                }
            }
            
            const item = this.playlist[this.currentIndex];
            
            if (item.filename.startsWith('!')) {                
                if (playlistId === this.playlistId) {
                    if (window.onHintPlaylistAttention) window.onHintPlaylistAttention(item.filename.slice(1)); 
                    this.currentIndex++;
                    this.playNextInPlaylist(playlistId);
                }
                return;                
            }
                
            // Checking the pause (file starts with :)
            if (item.filename.startsWith(':')) {
                const delay = parseInt(item.filename.substring(1));
                // end of block file mark (for shuffling)
                // {filename: ':0', speed: 1.0}                 
                if( delay != 0 ) {
                    setTimeout(() => {
                        // Checking that the playlist is still up to date
                        if (playlistId === this.playlistId) {
                            this.currentIndex++;
                            this.playNextInPlaylist(playlistId);
                        }
                    }, delay);
                }                    
                else {
                    if (playlistId === this.playlistId) {
                        this.currentIndex++;
                        this.playNextInPlaylist(playlistId);
                    }
                }
                return;
            }
            
            // Playing a regular file
            this.playFile(item.filename, item.speed || 1.0).then(success => {
                if (success) {
                    // currentIndex will increase after the end of the track (in onAudioEnded)
                } else {
                    // If there is a playback error, move on to the next one
                    if (playlistId === this.playlistId) {
                        this.currentIndex++;
                        this.playNextInPlaylist(playlistId);
                    }
                }
            });
        },
        
        // End of track handler
        onAudioEnded() {
            this.isPlaying = false;
            
            // If there is an active playlist
            if (this.playlist.length > 0 && this.playlistId > 0) {
                this.currentIndex++;
                this.playNextInPlaylist(this.playlistId);
            }
        },
       
        pause() {
            if (this.audio) {
                this.audio.pause();
                this.isPlaying = false;
            }
        },
                
        resume() {
            if (this.audio && !this.isPlaying && this.audio.currentTime > 0) {
                this.audio.play().then(() => {
                    this.isPlaying = true;
                }).catch(console.error);
            }
        },
                
        stop() {
            if (this.audio) {
                this.audio.pause();
                this.audio.currentTime = 0;
                this.audio.src = '';
            }
            
            this.playlist = [];
            this.playlistId = 0;
            this.currentIndex = 0;
            this.isPlaying = false;
        },
        
        // Skip the current track in the playlist
        skip() {
            if (this.playlist.length > 0) {
                if (this.audio) {
                    this.audio.pause();
                    this.audio.currentTime = 0;
                }
                this.currentIndex++;
                this.playNextInPlaylist(this.playlistId);
            }
        },
                
        getStatus() {
            return {
                isPlaying: this.isPlaying,
                playlistId: this.playlistId,
                currentIndex: this.currentIndex,
                playlistLength: this.playlist.length,
                currentTime: this.audio ? this.audio.currentTime : 0,
                duration: this.audio ? this.audio.duration : 0
            };
        }
    };
}



function playAudioSWeb(filename, speed) {
    if (!filename || filename.trim() === "") return;   
    if (window.onHintPlaylistCancel) window.onHintPlaylistCancel(); 
    // Using the manager for single playback
    window.audioSWebManager.playSingle(filename, speed || 1.0);
}

// Function for playing a list of files
function playAudioList(files, loop = false, shuffleN = 0) {    
    /* files - array of objects or strings: ['file1.mp3', 'file2.mp3']
    или
      [
        {filename: '!nameForAttention', speed: 1.0}, // call to the "window.onHintPlaylistAttention" function
        {filename: 'file1.mp3', speed: 1.0},
        {filename: ':1000', speed: 1.0}, // pause 1 second
        {filename: 'file2.mp3', speed: 1.5},
        {filename: ':0', speed: 1.0} // end of block file mark (for shuffling)
      ] 
    shuffleN - after how many cycles will the mixture be mixed    
    */        
    // Normalize the input data
    const normalizedFiles = files.map(item => {
        if (typeof item === 'string') {
            return { filename: item, speed: 1.0 };
        }
        return item;
    });    
    window.audioSWebManager.playPlaylist(normalizedFiles, loop, shuffleN);
}

function stopAllAudio() {
    window.audioSWebManager.stop();
}

function pauseAudio() {
    window.audioSWebManager.pause();
}

function resumeAudio() {
    window.audioSWebManager.resume();
}

// Skip the current track
function skipAudio() {
    window.audioSWebManager.skip();
}

function getAudioStatus() {
    return window.audioSWebManager.getStatus();
}
// ================
// ***** 251210 audio list player *****************
</script>



<script> // ***** 251210 CardDesign class ******************
/* =================== CardDesign class =================== */

if (!window.CardDesign) {    
window.CardDesign = class {
    constructor(cd_id) {
        this.id = cd_id;      
          
        this.version = "1.0";
        this.platform = this.detectAnkiPlatform();
        this.dataPar = {}; // Parameters for all currently viewed cards       
        this.data = {}; // Data entered on the face of the card        
        this.loadPar(); // Load parameters for all currently viewed cards    
        if(this.isAnswer())
            this.load();
        else
            this.save(); // clear as empty
 
        this.boundSave = this.save.bind(this);
        window.addEventListener("beforeunload", this.boundSave);       
        this.boundSaveIsHidden = this.saveIsHidden.bind(this);
        document.addEventListener("visibilitychange", this.boundSaveIsHidden);
        
        // hide elements not for this platform
        this.hideElementsPlatform();
        
    }
    
    
    destroy() {        
        window.removeEventListener("beforeunload", this.boundSave);
        document.removeEventListener("visibilitychange", this.boundSaveIsHidden);
    }
    
    isAnswer() {
        let el = document.getElementById("answer");
        if(el) {            
            return true;            
        }        
        return false;        
    }
    
    detectAnkiPlatform() {
        if (typeof pycmd !== "undefined") return "desk";
        if (typeof AnkiDroidJS !== "undefined") return "ankidroid";
        if (document.getElementById("qa_box")) return "ankiweb";
        return "ios";
    }
    
    save() {       
        try {            
            window.localStorage.setItem(
                "CardDesign_" + this.id,
                JSON.stringify({
                    data: this.data       
                })
            );
        } catch (e) {
            console.log("CardDesign.save error:", e);
        }
    }
    
    saveIsHidden() {
        if (document.hidden) this.save();    
    }

    load() {
        try {            
            const saved = window.localStorage.getItem("CardDesign_" + this.id);
            if (!saved) return;
            const obj = JSON.parse(saved);
            if (obj.data) this.data = obj.data;
        } catch (e) {
            console.log("CardDesign.load error:", e);
        }
    }
    
    savePar() {       
        try {
            window.localStorage.setItem(
                "CardDesign_Par_" + this.id,
                JSON.stringify({
                    data: this.dataPar     
                })
            );
        } catch (e) {
            console.log("CardDesign.savePar error:", e);
        }
    }

    loadPar() {
        try {
            const saved = window.localStorage.getItem("CardDesign_Par_" + this.id);
            if (!saved) return;
            const obj = JSON.parse(saved);
            if (obj.data) this.dataPar = obj.data;
        } catch (e) {
            console.log("CardDesign.loadPar error:", e);
        }
    }

    log(msg) {
        console.log(`[CardDesign v=${this.version}, app=${this.platform}] ${msg}`);
    }
    
    showAnswer() {
        if (this.platform == "desk") {            
            pycmd("ans");
        }
        else if (this.platform == "ankidroid") {
            window.showAnswer();
        }
        else if (this.platform == "ankiweb") {
            const btn = document.querySelector("#ansarea .btn");            
            if (btn) btn.click();
            else this.log("ERROR: Button not found in showAnswer()");
        }
    }    
    

    setData(key, value) {
        this.data[key] = value;
        this.save();
    }

    getData(key) {
        return this.data[key];
    }
    
    setPar(key, value) {
        this.dataPar[key] = value;
        this.savePar();
    }

    getPar(key) {
        return this.dataPar[key];
    }
    
    // hide elements not for this app or party
    hideElementsPlatform() {
        let Elements = null;
        if( this.platform == "desk") {
            Elements = document.getElementsByClassName('hideindesk');            
            for (let elem of Elements) elem.style= "display: none";                            
        }
        else if( this.platform == "ankidroid") {
            Elements = document.getElementsByClassName('hideinankidroid');
            for (let elem of Elements) elem.style= "display: none";
        }        
        else if( this.platform == "ankiweb") {
            Elements = document.getElementsByClassName('hideinankiweb');
            for (let elem of Elements) elem.style= "display: none";            
        }
        else if( this.platform == "ios") {
            Elements = document.getElementsByClassName('hideinios');
            for (let elem of Elements) elem.style= "display: none";            
        }
        
        if(this.isAnswer()) {
            Elements = document.getElementsByClassName('hideisback');
            for (let elem of Elements) elem.style= "display: none";            
        }
        else {            
            Elements = document.getElementsByClassName('hideisfront');
            for (let elem of Elements) elem.style= "display: none";            
        }
    }    
}}
/* ========↑↑↑======== CardDesign class ========↑↑↑======== */
// ***** 251210 CardDesign class ******************
</script>


<script> // ======================= MAIN ============================

window.cd = null;
window.cd = new window.CardDesign("20251128_"+`{{text:Speak->Learn}}`);
if( cd ) {    
    // what the user entered
    var elinpHTML = document.getElementById("inpHTML");
    if(elinpHTML) {        
        let vl = cd.getData("inpHTML"); 
        if(vl !== undefined) elinpHTML.innerHTML = vl;
        if(vl === undefined || vl == "") {
            elinpHTML.style.display = "none";
        }
        vl = cd.getData("inpHTMLClass");
        if(vl !== undefined) elinpHTML.classList.add(vl);    
    } 
    
    
    // FOR: answer sound 
    if(window.cd.platform == "ankiweb") {
        if (checkedCheckboxAS) {
            playAudioList([        
            {filename: '{{text:FileName_Audio_Learn}}', speed: 0.7},
            {filename: '{{text:FileName_Audio_Speak}}', speed: 1.0},
            {filename: '{{text:FileName_Audio_Learn}}', speed: 1.0}
            ]);
        }   
    }   
}

// ======================= MAIN ============================
</script> 


<script> // ***** 251210 drop-down menu ********************

/* ---- COPY ---- */
// Copy to clipboard for older browsers
function fallbackCopyToClipboard(text) {
  const textArea = document.createElement("textarea");
  textArea.value = text;
  textArea.style.position = "fixed"; // To prevent page scrolling
  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();    
  try {
    document.execCommand('copy');    
  } catch (err) {
    console.error('Clipboard write error: ', err);
  }  
  document.body.removeChild(textArea);
}

// The main function of copying to the clipboard
async function  copyToClipboard(text) {    
    if(window.cd.platform == "desk") {
        try {
            // An alternative method for older browsers           
            fallbackCopyToClipboard(text);            
        } catch(e) {
            await navigator.clipboard.writeText(text);            
        }   
    }
    else {
        try {
            await navigator.clipboard.writeText(text);
        } catch(e) {
            // An alternative method for older browsers           
            fallbackCopyToClipboard(text);
        }        
    }        
}
/* ^^^^ COPY ^^^^ */

if (!window.languageData) {
window.languageData = [
    { code: "AR", name: "العربية", codeGoogle: "ar", youglishName: "arabic" },
    { code: "DE", name: "Deutsch", codeGoogle: "de", youglishName: "german" },
    { code: "EM", name: "English US", codeGoogle: "en", youglishName: "" },
    { code: "EN", name: "English UK", codeGoogle: "en", youglishName: "" },
    { code: "ES", name: "español", codeGoogle: "es", youglishName: "spanish" },
    { code: "FR", name: "français", codeGoogle: "fr", youglishName: "french" },
    { code: "IT", name: "italiano", codeGoogle: "it", youglishName: "italian" },
    { code: "JA", name: "日本語", codeGoogle: "ja", youglishName: "japanese" },
    { code: "PT", name: "português PT", codeGoogle: "pt-PT", youglishName: "portuguese" },
    { code: "PX", name: "português BR", codeGoogle: "pt-BR", youglishName: "portuguese" },
    { code: "ZH", name: "中文", codeGoogle: "zh", youglishName: "chinese" },
    { code: "AD", name: "адыгабзэ", codeGoogle: "ady", youglishName: "" },
    { code: "AF", name: "Afrikaans", codeGoogle: "af", youglishName: "" },
    { code: "AM", name: "አማርኛ", codeGoogle: "am", youglishName: "" },
    { code: "BE", name: "беларуская", codeGoogle: "be", youglishName: "" },
    { code: "BG", name: "български", codeGoogle: "bg", youglishName: "" },
    { code: "BN", name: "বাংলা", codeGoogle: "bn", youglishName: "" },
    { code: "BS", name: "bosanski", codeGoogle: "bs", youglishName: "" },
    { code: "CA", name: "català", codeGoogle: "ca", youglishName: "" },
    { code: "CS", name: "čeština", codeGoogle: "cs", youglishName: "" },
    { code: "DA", name: "dansk", codeGoogle: "da", youglishName: "" },
    { code: "EL", name: "ελληνικά", codeGoogle: "el", youglishName: "greek" },
    { code: "EO", name: "esperanto", codeGoogle: "eo", youglishName: "" },
    { code: "ET", name: "eesti", codeGoogle: "et", youglishName: "" },
    { code: "FA", name: "فارسی", codeGoogle: "fa", youglishName: "persian" },
    { code: "FI", name: "suomi", codeGoogle: "fi", youglishName: "" },
    { code: "HE", name: "עברית", codeGoogle: "he", youglishName: "hebrew" },
    { code: "HI", name: "हिन्दी", codeGoogle: "hi", youglishName: "hindi" },
    { code: "HR", name: "hrvatski", codeGoogle: "hr", youglishName: "" },
    { code: "HU", name: "magyar", codeGoogle: "hu", youglishName: "" },
    { code: "HY", name: "հայերեն", codeGoogle: "hy", youglishName: "" },
    { code: "ID", name: "bahasa Indonesia", codeGoogle: "id", youglishName: "" },
    { code: "KA", name: "ქართული", codeGoogle: "ka", youglishName: "" },
    { code: "KK", name: "қазақша", codeGoogle: "kk", youglishName: "" },
    { code: "KN", name: "ಕನ್ನಡ", codeGoogle: "kn", youglishName: "" },
    { code: "KO", name: "한국어", codeGoogle: "ko", youglishName: "korean" },
    { code: "LT", name: "lietuvių", codeGoogle: "lt", youglishName: "" },
    { code: "LV", name: "latviešu", codeGoogle: "lv", youglishName: "" },
    { code: "MK", name: "македонски", codeGoogle: "mk", youglishName: "" },
    { code: "MR", name: "मराठी", codeGoogle: "mr", youglishName: "" },
    { code: "NL", name: "Nederlands", codeGoogle: "nl", youglishName: "dutch" },
    { code: "NN", name: "nynorsk", codeGoogle: "nn", youglishName: "" },
    { code: "NO", name: "norsk", codeGoogle: "no", youglishName: "" },
    { code: "PA", name: "ਪੰਜਾਬੀ", codeGoogle: "pa", youglishName: "" },
    { code: "PL", name: "polski", codeGoogle: "pl", youglishName: "polish" },
    { code: "RO", name: "română", codeGoogle: "ro", youglishName: "romanian" },
    { code: "RU", name: "русский", codeGoogle: "ru", youglishName: "russian" },
    { code: "SK", name: "slovenčina", codeGoogle: "sk", youglishName: "" },
    { code: "SL", name: "slovenščina", codeGoogle: "sl", youglishName: "" },
    { code: "SQ", name: "Shqip", codeGoogle: "sq", youglishName: "" },
    { code: "SR", name: "српски", codeGoogle: "sr", youglishName: "" },
    { code: "SV", name: "svenska", codeGoogle: "sv", youglishName: "swedish" },
    { code: "TA", name: "தமிழ்", codeGoogle: "ta", youglishName: "" },
    { code: "TE", name: "తెలుగు", codeGoogle: "te", youglishName: "" },
    { code: "TH", name: "ภาษาไทย", codeGoogle: "th", youglishName: "thai" },
    { code: "TI", name: "ትግርኛ", codeGoogle: "ti", youglishName: "" },
    { code: "TR", name: "Türkçe", codeGoogle: "tr", youglishName: "turkish" },
    { code: "UK", name: "українська", codeGoogle: "uk", youglishName: "ukrainian" },
    { code: "UR", name: "اردو", codeGoogle: "ur", youglishName: "" },
    { code: "VI", name: "Tiếng Việt", codeGoogle: "vi", youglishName: "vietnamese" }
];
}

// request for AI to clipboard
function getForII(txt, Speak, Learn) {
    
    function findNameByCode(code) {
        const upperCode = code.toUpperCase();
        const language = languageData.find(lang => lang.code === upperCode);        
        return language ? language.name : " ";
    }
    
    function findCodeGoogleByCode(code) {
        const upperCode = code.toUpperCase();
        const language = languageData.find(lang => lang.code === upperCode);        
        return language ? language.codeGoogle : " ";
    }
    
    let SpeakN = findCodeGoogleByCode(Speak);
    let LearnN = findCodeGoogleByCode(Learn);
    SpeakN = SpeakN + " (" + findNameByCode(Speak) + ")"; 
    LearnN = LearnN + " (" + findNameByCode(Learn) + ")";  
    
    retTxt = `This text is written in English.
I speak the language: ${SpeakN} (country code or language name) well.
I started learning the language: ${LearnN} (country code or language name)
There is a text in the language I am learning: ${txt}
Repeat this text in your answer on a separate line.
On a separate line below, provide a translation of this text into: ${SpeakN}
On another separate line, provide an example of its use (preferably a simple, uncomplicated sentence).
On the line below, provide a translation of the example (indicated on the line above) into: ${SpeakN}
On another line below, describe the rules in this text. Perhaps you can share some specific details about this text (taking into account the language I know well), so that it would be useful for those just beginning to learn this language.
When you give an answer, you don't need any additional words, like this is a translation, and this is an example, except for the last line where you describe the rules, where you can use different words for clarification`;
  
  copyToClipboard(retTxt);
}


/* When the user clicks the button,
toggle between hiding and showing the drop-down content */
function fDropDown() {
  navigator.vibrate(30); // vibration when pressed   
  document.getElementById("myDropdown").classList.toggle("show");
  var urlEl, yourLink, word = `{{text:Learn}}`;

  urlEl = document.getElementById("urlII");
  yourLink = "javascript:void(0);";
  urlEl.setAttribute('href', yourLink);
  speakLearn = `{{text:Speak->Learn}}`; // "EM->RU" — English USA->Russian
  const [SpeakLn, LearnLn] = speakLearn.split('->');    
  urlEl.onclick = function() {
      getForII(word, SpeakLn, LearnLn);      
  }; 
  
  function getLanguageByCode(code) {
    return languageData.find(lang => lang.code === code.toUpperCase());
  }  

  const speakLang = getLanguageByCode(SpeakLn);
  const learnLang = getLanguageByCode(LearnLn);
  
  const speakCodeLower = speakLang.codeGoogle;
  const learnCodeLower = learnLang.codeGoogle;
  
    
  urlEl = document.getElementById("urlFORVO");
  yourLink = "https://forvo.com/search/" + encodeURIComponent(word) + "/" + learnCodeLower + "/";
  urlEl.setAttribute('href', yourLink);
  
  urlEl = document.getElementById("urlYOUGLISH");  
  yourLink = "https://youglish.com/pronounce/" + encodeURIComponent(word) + "/" + learnLang.youglishName + "?";
  urlEl.setAttribute('href', yourLink);
  
  urlEl = document.getElementById("urlGOOGLE");
  yourLink = "https://translate.google.com/?hl=" + speakCodeLower + 
             "&sl=" + learnCodeLower + 
             "&tl=" + speakCodeLower + 
             "&text=" + encodeURIComponent(word);
  urlEl.setAttribute('href', yourLink);
    
  urlEl = document.getElementById("urlYANDEX"); 
  yourLink = "https://translate.yandex.ru/?source_lang=" + learnCodeLower + 
             "&target_lang=" + speakCodeLower + 
             "&text=" + encodeURIComponent(word);
  urlEl.setAttribute('href', yourLink);
  
  urlEl = document.getElementById("urlWORDREF"); 
  yourLink = "https://www.wordreference.com/" + learnCodeLower + speakCodeLower
    + "/" + encodeURIComponent(word);
  urlEl.setAttribute('href', yourLink);
  
} 


elmyDropdown = document.getElementById("myDropdown");
if(elmyDropdown) {
    elmyDropdown.innerHTML =
        `<a id="urlII" href="#">FOR AI? (to the clipboard)</a>`    
        + `<a id="urlFORVO" href="#">FORVO (voice)</a>`        
        + `<a id="urlYOUGLISH" href="#">YOUGLISH (video subtitles)</a>`        
        + `<a id="urlGOOGLE" href="#">GOOGLE (translation)</a>`
        + `<a id="urlYANDEX" href="#">YANDEX (translation)</a>`
        + `<a id="urlWORDREF" href="#">WORDREF (translation)</a>`;
}


// Close a drop-down menu if the user clicks outside of it
if(!window.f_wonclick) {
    window.f_wonclick = true;
    window.onclick = function(event) {
      if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
          }
        }
      }
    }
}
    


// ***** 251210 drop-down menu ********************
</script>


<script> // ***** 251210 <audio> with the standard button ********
// depends: CardDesign class, audio list player  
// === for «ankiweb»! ===
// === replacing the display <audio> with the standard button view ===
(function() {
    if(window.cd.platform == "ankiweb") {
        // Find all tags <audio>
        let audios = document.querySelectorAll("audio");
        audios.forEach(function(audio) {          
            if (audio.getAttribute("controls") !== "") return;
    
            // Let's check what's inside <source>
            let srcEl = audio.querySelector("source");
            if (!srcEl) return;
    
            let src = srcEl.getAttribute("src");
            if (!src) return;
            
            
            // We check to make sure we don't insert the button again.
            if (audio.nextElementSibling && audio.nextElementSibling.classList.contains("replay-button")) {
                return;
            }
                
            let a = document.createElement("a");
            a.className = "replay-button soundLink";            
            a.setAttribute("onclick", "stopAllAudio(); setTimeout(() => { playAudioSWeb('" + src + "', 1) }, 50); return false;");
            a.setAttribute("draggable", "false");
            
            a.innerHTML = `            
                <svg class="playImage" viewBox="0 0 64 64" version="1.1">
                    <circle cx="32" cy="32" r="29"></circle>
                    <path d="M56.502,32.301l-37.502,20.101l0.329,-40.804l37.173,20.703Z"></path>                    
                </svg>
            `;    
            
            audio.insertAdjacentElement("afterend", a);
            audio.style.display = "none";
            if (!audio.paused) {
                audio.pause();
            }
            audio.parentNode.removeChild(audio); // audio.remove();
        });    
    }
})();
// ================
// ***** 251210 <audio> with the standard button ********
</script> 


<script> // ***** 251210 show all languages *****************
// gets all data for the index
async function lookupWordAllLangs(index = '') {   
    try {
        // Download once and cache
        if (!window._vocabCache) {
            const response = await fetch("_book2_note_p.json");
            window._vocabCache = await response.json();
        }
        
        // Get all languages ​​for a given index
        const allLangsData = window._vocabCache?.[index];
        if (allLangsData) {
            return allLangsData; //  {en: {...}, ru: {...}, ...}
        }
        return null;
    } catch (error) {
        console.error('ERROR:', error);
        return null;
    }
}

// Function to get a specific language (if needed)
async function lookupWord(index = '', lang = '') {
    const allLangs = await lookupWordAllLangs(index);
    if (allLangs && allLangs[lang]) {
        return { word: allLangs[lang].w, note: allLangs[lang].p };
    }
    return null;
}


function allTranslations(listLn = '', cntLn = 0) {
    // Checking if the container is displayed
    const container = document.querySelector('.allTrans');    
    let btnHBLoop = document.getElementById("btnHintBackLoop");
    // If the container is visible and was opened with this button, hide it and exit.   
    if (container.style.display !== 'none' && container.dataset.cntlnstr == String(cntLn)) {
        container.style.display = 'none';     
        if(btnHBLoop) btnHBLoop.style.display = 'none'; 
        container.classList.remove('translation-active');
        // Remove the active class from all elements
        document.querySelectorAll('.translation-item.active').forEach(el => {
            el.classList.remove('active');
        });
        delete container.dataset.cntlnstr;
        return;
    }
    
    container.dataset.cntlnstr = String(cntLn);
    
    // We receive data
    let index = `{{text:ID-number}}`;
    let speakLearn = `{{text:Speak->Learn}}`;
    let [SpeakLn, LearnLn] = speakLearn.split('->');
    
    // Getting a list of languages ​​to display
    let languages = listLn.split(',').filter(lang => 
        lang.trim() !== ''
        /* && lang !== SpeakLn
        && lang !== LearnLn */
    );
    
    // If cntLn > 0, limit the quantity (except SpeakLn and LearnLn)
    if (cntLn > 0) {
        languages = languages.slice(0, cntLn);
    }
    
    // If there are no languages ​​to display, exit.
    if (languages.length === 0) {
        console.log('There are no languages ​​to display.');
        return;
    }
        
    lookupWordAllLangs(index).then(allLanguagesData => {
        if (!allLanguagesData) {
            console.log(`Data for index ${index} not found`);
            return;
        }
        
        // Generating HTML
        let html = '';
        
        // We go through the required languages
        languages.forEach(lang => {
            const entry = allLanguagesData[lang];
            if (entry) {
                const langName = getLangName(lang);
                const soundName = 'book2_phr_N' + index + '_' + lang + '.mp3';
                const idwt = entry.w + "#" + lang; 
                html += `
                <div class="translation-item" data-lang="${lang}"  data-word="${entry.w}" data-fnword="${soundName}" data-idwt="${idwt}" onclick="playTranslationSound('${index}', '${lang}', this)">
                    <div class="language-label">${langName.toLowerCase()}:&nbsp;</div><div class="translation-item-word">`;
                
                if (entry.p && entry.p.trim() !== "") {
                    html += `${entry.w} (${entry.p})`;
                } else {
                    html += `${entry.w}`;
                }
                
                html += `</div></div>`;
            }
        });
        
        container.innerHTML = html;                
        container.style.display = 'inline-block';
        btnHBLoop.style.display = 'inline-block';
        container.classList.add('translation-active');
        
    }).catch(error => {
        console.error('Error loading translations:', error);
    });
}


// play all the prompts in a loop
function playAllHintBackLoop(event) {
    let elB = event.target;
    if(elB.classList.contains("active")) {
        elB.classList.remove('active');
        if (window.onHintPlaylistCancel) window.onHintPlaylistCancel();
        stopAllAudio();
        return;
    }
    const btns = document.querySelectorAll(".allTrans .translation-item");
    let listP = [];    
    for (let i = 0; i < btns.length; i++) {
        const btn = btns[i];
        if(btn.dataset.word && btn.dataset.word.trim() !== "") {
            // Adding files to the list
            listP.push(
                {filename: '!'+String(btn.dataset.idwt), speed: 1.0}, // call to the "window.onHintPlaylistAttention" function                
                {filename: btn.dataset.fnword || '', speed: 1.0},
                {filename: ':1000', speed: 1.0}, // pause 1 second
                {filename: ':0', speed: 1.0}// end of block file mark (for shuffling)
            );
        }
    }
    
    // Filter empty files (just in case)
    listP = listP.filter(item => item.filename.trim() !== '');    
    if (listP.length > 0) {        
        if (window.onHintPlaylistStart) window.onHintPlaylistStart();         
        playAudioList(listP, true, 0); // true = looping; 3 = shuffle after 3 repetitions of the list
    } else {
        console.log('There are no files to play.');
    }
}


window.onHintPlaylistStart = function() {
    const btn = document.getElementById('btnHintBackLoop');
    if (btn) btn.classList.add('active');
};

window.onHintPlaylistCancel = function() {
    const btn = document.getElementById('btnHintBackLoop');
    if (btn) btn.classList.remove('active');    
};

window.onHintPlaylistAttention = function(idA) {
    // select the recording being played
    const btns = document.querySelectorAll(".allTrans .translation-item");    
    for (let i = 0; i < btns.length; i++) {
        const btn = btns[i];                
        if(btn.dataset.idwt !="" && btn.dataset.idwt == idA) {                
            btn.classList.add("active");             
        } 
        else {
            btn.classList.remove("active");
        }
        //void btn.offsetWidth; // for redrawing
    }
};



// Function to play a sound when clicking on a translation
function playTranslationSound(index, lang, element) {    
    stopAllAudio();  
    // Remove the active class from all elements
    document.querySelectorAll('.translation-item.active').forEach(el => {
        el.classList.remove('active');
    });
    element.classList.add('active');
    const soundName = 'book2_phr_N' + index + '_' + lang + '.mp3';      
    playAudioSWeb(soundName, 1);
}

function getLangName(code) {
    const langNames = {
        'AR': 'ar', 'BG': 'bg', 'DE': 'de', 'EM': 'en',
        'EN': 'en', 'ES': 'es', 'FR': 'fr', 'IT': 'it',
        'JA': 'ja', 'KO': 'ko', 'PL': 'pl', 'PX': 'pt-br',
        'RO': 'ro', 'RU': 'ru', 'TR': 'tr', 'UK': 'uk',
        'ZH': 'zh'
    };
    return langNames[code] || code.toLowerCase();
}

// ***** 251210 show all languages *****************
</script>


<script>
elstatusSL = document.getElementById('statusSL');
if(elstatusSL) elstatusSL.innerHTML = `{{text:Speak->Learn}}`.replace('->', '−>');
elS = document.getElementById('id_wordS');
elL = document.getElementById('id_wordL');
if(elS && elL) {
    speakLearn = `{{text:Speak->Learn}}`; // "EM->RU" — English USA->Russian
    const [SpeakLn, LearnLn] = speakLearn.split('->');  
    if(SpeakLn == 'AR') elS.classList.add('AR');
    if(LearnLn == 'AR') elL.classList.add('AR');    
}
</script>

""",
        },
    ],
    css="""
.card {
    font-family: arial;
    font-size: 20px;
    line-height: 1.5;
    text-align: center;
    color: black;
    background-color: white !important;
    letter-spacing: 0.07em;
    --parWhite: #ffffff;
    --parYellow: #ffff7f; 
    --parbgCard: white; 
}

div {
    position: relative;
}

summary {
    color: #aaaaaa77 !important;    
}
a.hint {
    color: black;
    font-family: arial;
    font-size: 18px;
}
.nightMode a.hint {
    color: #eeeeee;
}


.card.nightMode {
    background-color: black !important;   
    --parbgCard: black;      
} 

.bgYellow {
    background-color: var(--parYellow);   
}
.bgCard {
    background-color: var(--parbgCard);    
}


.inFrame {
    display: inline-block;
    padding:5px 15px;
    border: 2px solid gray;
    margin: 0px;    
}


#answer {
    margin: 1px 0px 5px 0px;
    padding: 0px;
}


.chBox, #checkboxAS, #checkboxH10, #checkboxAF {
    user-select: none;
}


.psound {    
    user-select: none;
    display: inline-flex !important;
    vertical-align: middle !important;
    align-content: center !important;
    align-items: center !important;
    flex-direction: row !important;
    /* margin: 5px !important; */
    padding: 5px !important;
}

.replay-button, .replay-buttonMy, .soundLink {
    zoom: 1.0 !important;
    text-decoration: none;    
    vertical-align: middle !important;   
    cursor: pointer;
    margin: 0px !important;
    padding: 0px !important;     
    width: 32px !important;
    height: 32px !important;
    min-width: 20px !important; 
    min-height: 20px !important;     
}

.replay-button span {
    margin: 0px !important;
    padding: 0px !important;
}

.replay-button svg, .replay-buttonMy svg  {
    width: 32px !important;
    height: 32px !important;
    min-width: 20px !important; 
    min-height: 20px !important; 
    
    vertical-align: middle !important;
    align-content: center !important;
    align-items: center !important;     
}


.replay-button svg circle, .replay-buttonMy svg circle {
  fill: lightgray;
  stroke: black;
}
.replay-button svg path, .replay-buttonMy svg path {
  stroke: white;
  fill: black;
}
.replay-buttonMy.active svg path {
  stroke: white;
  fill: #8f0000;
}

p {
    margin: 5px !important;
    line-height: 1.5;    
}

.word_speak {  
    font-size: 24px;
    letter-spacing: 0.1em; 
    line-height: 1.5;        
    margin: 0px;    
    /* height: auto;
    display: contents; */
}

.word_learned {
    font-size: 24px;
    font-weight: 600;
    letter-spacing: 0.1em;  
    vertical-align: middle;  
    margin: 0px;
    padding: 0px;
    color: black;
}


@keyframes unmaskR {
    from {
        transform: translateX(0);
    }
    to {
        transform: translateX(100%);
    }
}

@keyframes unmaskL {
    from {
        transform: translateX(0);
    }
    to {
        transform: translateX(-100%);
    }
}

.showWordSlowly {
    position: relative;
    display: inline-block;
    overflow: hidden;    
}

.showWordSlowly::after {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    width: 120%;
    height: 100%;
    pointer-events: none;    
    background: linear-gradient(
        to right,
        color-mix(in srgb, var(--ws-bcolor, var(--parYellow)) 100%, transparent 0%) 100%,
        color-mix(in srgb, var(--ws-bcolor, var(--parYellow)) 0%, transparent 100%) 100%
    );
}
.showWordSlowly::after {
    animation: unmaskR
        var(--ws-duration, 1s)  
        linear 
        forwards
        var(--ws-delay, 0s);     
}

.showWordSlowly.AR::after {
    animation: unmaskL
        var(--ws-duration, 1s)  
        linear 
        forwards
        var(--ws-delay, 0s); 
}



.fadeMaskW, .fadeMaskY, .fadeMaskYW1s, .fadeMaskYW0s {
    position: relative;
    display: inline-block;
    overflow: hidden;
}

.fadeMaskYW1s::after, .fadeMaskYW0s::after, .fadeMaskY::after {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    width: 120%;
    height: 100%;
    pointer-events: none;
    
    background: linear-gradient(
        to right,
        rgba(255, 255, 127, 1) 100%,
        rgba(255, 255, 127, 0) 100%  
    );    
}

/* animation, speed of displaying words !!! */
.fadeMaskYW1s::after {
    animation: unmaskR 1.5s linear forwards 1s;
}

.fadeMaskYW0s::after {
    animation: unmaskR 1.5s linear forwards 0s;
}

.fadeMaskY::after {
    animation: unmaskR 2.5s linear forwards;
}
.fadeMaskW::after {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    width: 120%;
    height: 100%;
    pointer-events: none;

    background: linear-gradient(
        to right,
        rgba(255, 255, 255, 1) 100%,
        rgba(255, 255, 255, 0) 100%
    );

    animation: unmaskR 1s linear forwards;
}

.nightMode .fadeMaskW::after {
		background: linear-gradient(
        to right,
        rgba(0, 0, 0, 1) 100%,
        rgba(0, 0, 0, 0) 100%
    );		
} 





.tab_wl {
    border-style: solid !important;
    background-color: var(--parYellow) !important;
    padding: 0.2em;
    border-width: 2.5px !important;
}
.nightMode .tab_wl {
    color: black;     
    background-color: var(--parYellow) !important; 
    border-color: #949494;
    
}

.inputSD {
    text-indent: 0px !important;     
    /* background-color: #000000 !important; */
    font-family: arial !important;
    font-size: 20px !important;
    font-weight: bold !important;
    letter-spacing: 0.1em !important;
    text-align: center;    
    width: 95%;
    line-height: 1.5;
    padding: 4px;
}

.goodInput {
    color: green;    
}
.ErrorInput {
    color: red;    
}
.colorInput {
    color: black;    
}
.nightMode .colorInput {
    color: #00aeff;    
}

.note {
    font-size: 16px;
    font-weight: 400;
}

.imageWord {
    cursor: pointer;    
}

audio {
    height: 30px;
    vertical-align: middle;
}

.audio-box {
  display: flex;
  gap: 2px;
  font-size: 0;
}

.audio-btn {  
  padding: 6px 6px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  background: #4a90e2;
  color: white;
  font-size: 14px;
  transition: transform 0.1s, background 0.1s;
    min-width: 30px;
    max-width: 36px;
    transform: scale(1.05);
}

.audio-btn.active {
  background: #2d6fb5;
  transform: scale(0.97);
}


.editable {
    text-indent: 0px !important;        
    font-family: arial !important;
    font-size: 20px !important;
    font-weight: bold !important;
    letter-spacing: 0.1em !important;
    text-align: center;    
    width: 95%;
    line-height: 1.5;
    padding: 4px;
    
    border: 1px solid gray;
    /* padding: 2px; */
    min-height: 20px;
    white-space: pre;
    margin: auto;           
}





/* ============ ↓↓↓ REGULATOR FOR 3 ======================= */
.js {
    --js: 1 ;
}

.wrap {
    display: grid;
    margin: 0 auto 0;
    padding: 0;
    font: inherit;
    width: 100%;  
    max-width: 450px;
}

.wrap--2x {
    --j: var(--js, 0);
    align-content: end;
    grid-gap: 0.25em;  
    place-self: center;
    min-width: 8em;
    /*width: calc(100% - 1.5em);*/
    width: calc(100%) !important;
    height: 0.5rem;  
    border-radius: 0rem !important;
    font: 500 0.7em ubuntu, trebuchet ms, sans-serif;
    filter: Saturate(var(--hl, 0));
    transition: filter 0.3s;
}
.wrap--2x::before, .wrap--2x::after {
    margin: 0.5rem 0rem !important;
    border-radius: 0rem !important;
    box-shadow: inset 0 1px 2px #cbcbcb, 0 1px 1px #fefefe;
    background: linear-gradient(#d9d9d9, #e1e1e1);
    content: "";
}
.wrap--2x::after {
    --or: calc((100 - Max(var(--a), var(--b)))*1%);
    --ol: calc(Min(var(--a), var(--b))*1%);
    --op: calc((100 - var(--p))*1%);  
    background: #004400;
    clip-path: inset(0 var(--op) 0 0%);
}
.wrap--2x input, .wrap--2x::before, .wrap--2x::after {
    grid-area: calc(1 + var(--j))/1;  
}
.wrap--2x output, .wrap--2x::after {
    display: var(--js, none);
}
.wrap--2x:focus-within, .wrap--2x:hover {
    --hl: 1 ;
}

.wrap [type=range] {
    width: 100%;
    height: 1.5rem;
    background: transparent;
    pointer-events: none;
    padding: 0px;
    margin: 0px 0px 0px 0px;
}

.wrap [type=range] {
    -webkit-appearance: none;    
}

.wrap [type=range], .wrap [type=range]::-webkit-slider-runnable-track, .wrap [type=range]::-webkit-slider-thumb {
    -webkit-appearance: none;
} 

.wrap [type=range]::-moz-range-track, .wrap [type=range]::-moz-range-thumb {
    -moz-appearance: none;
}

.wrap [type=range], .wrap [type=range] + output {
    /*--sel: 0;*/
    /*z-index: calc(1 + var(--sel));*/
}

/* [type=range]::-webkit-slider-runnable-track {
    background: transparent;
}
[type=range]::-moz-range-track {
    background: transparent;
} */


.playAB::-webkit-slider-thumb {
    -webkit-appearance: none;  
    width: 0.5rem !important;
    height: 1.2rem !important;
    background: #aaaaaaaa !important;
    border: 0px !important;
    pointer-events: auto;
    cursor: ew-resize;    
    margin: 0px !important;
    padding: 0px !important;  
}

.playAB::-moz-range-thumb {
    -moz-appearance: none; 
    width: 0.5rem !important;
    height: 1.2rem !important;
    background: #aaaaaaaa  !important;
    border: 0px !important;
    pointer-events: auto;
    cursor: ew-resize;    
    margin: 0px !important;
    padding: 0px !important;  
}

 
.playAB:focus::-webkit-slider-thumb {
    -webkit-appearance: none;
    background: blue  !important;    
}

.playAB:focus::-moz-range-thumb {
    -moz-appearance: none;
    background: blue  !important;    
}


.playpoint::-webkit-slider-thumb {  
    -webkit-appearance: none;  
    background: #007700  !important;
    pointer-events: auto !important;
    cursor: ew-resize !important; 
    width: 0.5rem !important;
    height: 0.5rem !important;
    margin: 0px !important;
    padding: 0px !important;     
    border: 2px !important;    
}

.playpoint:focus::-webkit-slider-thumb { 
    -webkit-appearance: none;  
    background: blue !important;        
    pointer-events: auto !important;
    cursor: ew-resize !important; 
    width: 0.5rem !important;
    height: 0.5rem !important;
    margin: 0px !important;
    padding: 0px !important;;     
    border: 2px !important; 
}

.playpoint::-moz-range-thumb {
    -moz-appearance: none;
    background: #007700  !important;
    pointer-events: auto !important;
    cursor: ew-resize !important; 
    width: 0.5rem !important;
    height: 0.5rem !important;
    margin: 0px !important;
    padding: 0px !important;;     
    border: 2px !important; 
}

.playpoint:focus::-moz-range-thumb { 
    -webkit-appearance: none;     
    background: blue !important;        
    pointer-events: auto !important;
    cursor: ew-resize !important; 
    width: 0.5rem !important;
    height: 0.5rem !important;
    margin: 0px !important;
    padding: 0px !important;;     
    border: 2px !important;  
}


.wrap [type=range]:focus {
    outline: none;
}
.wrap [type=range]:focus, .wrap [type=range]:focus + output, .wrap [type=range]:hover, .wrap [type=range]:hover + output {
    /*--sel: 1;*/
}
.wrap [type=range] + output {   
    --pos: calc( -0.2rem + (.01*var(--c)*(100% - 1.2rem)) );  
    grid-area: 1/1;
    justify-self: start;
    margin-left: var(--pos);
    transform-origin: 50% 100%;
    transform: translate(-50%) scale(var(--sel));
    counter-reset: c var(--c);
    /* filter: drop-shadow(1px 2px 2px #bcbcbc); */
    transition: transform 0.3s ease-out; 
}

.wrap [type=range] + output::after {    
    display: grid;  
    padding: 0px;
    margin: 0px;
    border-radius: calc(0.5rem + 4px);
    color: #616161;
    font-size: 0.875em;      
    mask: var(--mask);
    content: counter(c) "%";
}

#outP, #outP::after {
    margin-top: 5px;
    content: counter(c) "%"; 
}

/* ============ ↑↑↑ REGULATOR FOR 3 ======================= */



/* ============ ↓↓↓ myRange ======================= */
.range-wrap {
    position: relative;
    max-width: 250px;
    min-width: 50px;
    width: 100%;
    display: inline;
}

.range-value {
    position: absolute;
    top: -10px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 0.7rem;
    pointer-events: none;
    color: #aaaaaa;
}

.myRange {
    -webkit-appearance: none;
    -moz-appearance: none;
    max-width: 150px;
    height: 6px;
    background: #ddd;          /* base background */
    border-radius: 3px;
    outline: none;
}

/* ============ Chrome / Edge / Safari ============ */
.myRange::-webkit-slider-runnable-track {
    height: 6px;
    background: #ddd;
    border-radius: 3px;
}

.myRange::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: radial-gradient(circle, #aaa, #000);
    border-width: 0px;
    cursor: pointer;
    margin-top: -5px;
}

/* Filling to value */
.myRange::-webkit-slider-runnable-track {
    -webkit-appearance: none;
    background: linear-gradient(to right, #7f97b0 0 var(--val), #ddd var(--val) 100%) !important;
}

/* ============ Firefox ============ */
/* трек */
.myRange::-moz-range-track {
    height: 6px;
    background: #ddd;
    border-radius: 3px;
}

/* fill (from min to value!) */
.myRange::-moz-range-progress {
    height: 6px;
    background: #7f97b0;
    border-radius: 3px;
}

/* thumb */
.myRange::-moz-range-thumb {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: radial-gradient(circle, #aaa, #000);
    border-width: 0px;
    cursor: pointer;
}

/* ============ ↑↑↑ myRange ======================= */
.grcontrrange {
    display: inline-block;   
}

.control1 {
    display: inline;
    align-content: center;
    align-items: center;
    max-width: 500px;    
}
.textcontrol {
    margin-top: 10px;
    font-size: 0.7rem;
    display: inline;
}

.rowtime {
    font-size: 14px;
}



/*  MAIN BUTTONS */
.control2 .controls-row {
    display:flex; gap:8px;
    flex-wrap:wrap;
    justify-content: center;    
}

.control2 .ctrl {
  padding:3px 3px;
  border-radius:6px;
  border:1px solid #ccc;
  background:#f5f5f5;
  cursor:pointer;
  font-size:12px;
  color: black;
  width: 35px;
  height: 30px;
  position: relative;
  user-select: none;
}

.control2 .ctrl[disabled] { opacity:0.45; cursor:not-allowed; }
.control2 .ctrl.toggle.active { background:#adcae9; color:#000; border-color:#adcae9; }
.control2 .ctrl.active { background:#adcae9; }

.smallvalue {
  position: absolute;
  left: 2px;
  top: 0px;
  font-size: 9px;
  color: black;
  opacity: 1;
}

.submenu-caret {
  position: absolute;
  right: 1px;
  bottom: -1px;
  font-size: 8px;
  opacity: 0.4;
  color: black;
  transform: rotate(90deg);
}


.btnSug, .btnClear {
    user-select: none;
}


.hintblock {    
    display: flex;
    /* align-content: center; */
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    margin-top: 15px;
    /* flex-direction: row; */    
}

.spbtnHints {
    font-size: 14px !important;    
    font-family: arial;
    padding: 7px;
    opacity: 1;
    margin: 0px;
}

.btnHints, .btnHintsLoop {
    line-height: 1.5;
    font-size: 14px !important; 
    font-family: arial;
    letter-spacing: 0.07em; 
    margin: 0px;
    /* font-weight: bold !important; */    
    min-height: 52px;
    min-width: 52px;
    padding: 5px 10px !important;
    border-radius: 5px !important;     
    box-shadow: 
    0 1px 3px rgba(0, 0, 0, 0.12),
    0 1px 2px rgba(0, 0, 0, 0.24) !important;
    border-color: #cecece;   
    color: black;
    user-select: none;
}


    
.nightMode .btnHints, .nightMode .btnHintsLoop {
    border-color: #848484;
    background: #1f1f1f;
    color: white;    
    border-width: 0.5px;}
    
.errtrans {
    /* color: black !important;  */       
    /* font-weight: bold !important; */     
}
.truetrans, .truetrans:hover {
    color: black !important;  
    /* font-weight: bold !important; */
    background: var(--parYellow) !important;
}

.playAttention, .playAttention:hover {
    color: black !important;  
    /* font-weight: bold !important; */
    background: var(--parYellow) !important;
}

.spbtnHints:has(.btnHints.errtrans),
.spbtnHints:has(.btnHints.truetrans) {
    opacity: 1;
}

#btnHintLoop.active {
    background: #5997c7 !important;    
}



/* ============ ↓↓↓ drop-down menu ======================= */
.dropdown {  
    display: inline-block;
    font-size: 14px;  
    user-select: none;     
}

.dropdown-content {
  display: none;
  user-select: none;
  text-align: center;  
  position: absolute;
  transform: translate(-40%, 0%);
  background-color: #f1f1f1;
  min-width: 250px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 10000; /* since on the website https://ankiuser.net/ 9999 to select the difficulty */  
}

/* Links inside a drop-down list */
.dropdown-content a {
  color: black;
  padding: 8px 8px;
  text-decoration: none;
  display: block;
  user-select: none;
}

.nightMode .dropdown-content {
    background-color: #555555;
}
.nightMode .dropdown-content  a {
    color: white;
}

/* Change the color of drop-down links when hovering over them */
.dropdown-content a:hover {background-color: #ddd}
.nightMode .dropdown-content a:hover {background-color: #333333}
.nightMode

/* Show drop-down menu */
.show, .dropdown-content.show {
    display: block;
}

.dropbtn {
    border-radius: 6px;
}

/* ============ ↑↑↑ drop-down menu ======================= */


/* ============ ↓↓↓ show all languages =================== */
.divAllTrans {
    opacity: 0.2;
    position: absolute;
    right: 0px;
    top: 0px;
    margin: 0px;   
    z-index: 1019;       
    user-select: none !important;
}
.divAllTrans button {
    font-size: 14px;    
    min-width: 25px;
    min-height: 20px;       
    margin: 0px 5px 0px 10px;             
    user-select: none !important;      
}
.allTrans {
    font-family: arial;
    font-size: 18px;
    text-align: center;
    margin: 10px 0;
    padding: 10px;
    border-radius: 5px;    
    user-select: none !important;    
}
.allTrans.translation-active {
    display: block !important;
}

.translation-item {    
    user-select: none !important;
    display: inline-block;
    margin: 5px 10px;
    padding: 8px 15px;
    border-radius: 0px;    
    cursor: pointer;    
    /* transition: background-color 0.1s; */
    white-space: nowrap;
}

.translation-item-word {
    user-select: none !important;
    padding: 5px;    
    display: inline-block;
    border: 2px solid #55555501;
}

.active .translation-item-word {
    user-select: none !important; 
    color: black;
    background-color: var(--parYellow, #ffff7f) !important;  
    border: 2px solid #555555;
    /* font-weight: bold; */
}

.translation-item:hover, .translation-item:focus, .translation-item:active {
    user-select: none !important;
    background-color: #e0e0e033;
    color: black;    
}



.language-label {
    display: inline-block;
    user-select: none !important;
    color: #666;
    font-size: 0.9em;
    margin-right: 5px;
    opacity: 0.3;
}

#btnHintBackLoop.active {
    background: #5997c7 !important;    
}

/* ============ ↑↑↑ show all languages ======================= */

""",    
)
