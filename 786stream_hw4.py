import streamlit as st

st.title("Gyroscope Sensor Readings")
st.markdown("""
This app displays real-time gyroscope sensor readings (X, Y, Z axes) and logs them.  
Ensure you allow device orientation permissions.
""")

gyro_script = """
<script>
let logData = [];

function handleOrientation(event) {
    const x = event.beta;    // Front-to-back tilt in degrees
    const y = event.gamma;   // Left-to-right tilt in degrees
    const z = event.alpha;   // Rotation around the z-axis in degrees

    document.getElementById("x-axis").innerHTML = `X-axis: ${x.toFixed(2)}°`;
    document.getElementById("y-axis").innerHTML = `Y-axis: ${y.toFixed(2)}°`;
    document.getElementById("z-axis").innerHTML = `Z-axis: ${z.toFixed(2)}°`;

    // Log data
    const timestamp = new Date().toISOString();
    logData.push({ timestamp, x: x.toFixed(2), y: y.toFixed(2), z: z.toFixed(2) });
    if (logData.length > 100) { // Limit log size to 100 entries
        logData.shift();
    }

    // Update log display
    const logElement = document.getElementById("gyro-log");
    logElement.innerHTML = logData.map(entry => 
        `<div>[${entry.timestamp}] X: ${entry.x}°, Y: ${entry.y}°, Z: ${entry.z}°</div>`
    ).join('');
}

if (window.DeviceOrientationEvent) {
    window.addEventListener("deviceorientation", handleOrientation);
} else {
    document.getElementById("x-axis").innerHTML = "Device orientation not supported.";
    document.getElementById("y-axis").innerHTML = "";
    document.getElementById("z-axis").innerHTML = "";
}
</script>
<div>
    <p id="x-axis">X-axis: Waiting for data...</p>
    <p id="y-axis">Y-axis: Waiting for data...</p>
    <p id="z-axis">Z-axis: Waiting for data...</p>
</div>
<h3>Logged Data:</h3>
<div id="gyro-log" style="height: 200px; overflow-y: scroll; border: 1px solid #ddd; padding: 10px;">
    Waiting for log data...
</div>
"""

st.components.v1.html(gyro_script, height=400)
