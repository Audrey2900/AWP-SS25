import streamlit as st

def render():
    st.components.v1.html("""
        <div id="timerDisplay" style="
            font-size: 20px; 
            font-weight: bold; 
            margin-bottom: 10px; 
            color: darkred;
            font-family: sans-serif;
        ">
            ⏳ Zeit bis Inaktivität: <span id="countdown">300</span> Sekunden
        </div>

        <script>
        let inactivityTime = function () {
            let countdown = 300;
            let countdownInterval;
            let timeout;

            const display = document.getElementById("countdown");

            const updateCountdown = () => {
                if (display) display.innerText = countdown;
            };

            const resetTimer = () => {
                clearTimeout(timeout);
                clearInterval(countdownInterval);

                countdown = 300;
                updateCountdown();

                countdownInterval = setInterval(() => {
                    countdown--;
                    updateCountdown();
                    if (countdown <= 0) {
                        clearInterval(countdownInterval);
                        parent.window.location.reload();
                        console.log("User ist inaktiv!");
                    }
                }, 1000);
            };

            ['mousemove', 'keydown', 'click', 'scroll', 'wheel', 'touchmove'].forEach(event => {
                parent.document.addEventListener(event, resetTimer);
            });

            resetTimer();
        };

        inactivityTime();
        </script>
    """, height=0)
