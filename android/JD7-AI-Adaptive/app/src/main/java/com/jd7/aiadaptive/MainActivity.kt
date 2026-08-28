package com.jd7.aiadaptive

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.height
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.jd7.aiadaptive.monitor.DeviceMonitor
import com.jd7.aiadaptive.monitor.DeviceSnapshot

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val monitor = DeviceMonitor(applicationContext)

        setContent {
            JD7Dashboard(monitor)
        }
    }
}

@Composable
private fun JD7Dashboard(monitor: DeviceMonitor) {
    var monitoring by remember { mutableStateOf(false) }
    var snapshot by remember { mutableStateOf<DeviceSnapshot?>(null) }

    LaunchedEffect(monitoring) {
        if (monitoring) {
            while (true) {
                snapshot = monitor.snapshot()
                kotlinx.coroutines.delay(5_000)
            }
        }
    }

    MaterialTheme {
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(24.dp),
            verticalArrangement = Arrangement.Center
        ) {
            Text(
                text = "JD7 AI Adaptive",
                style = MaterialTheme.typography.headlineMedium
            )
            Spacer(Modifier.height(8.dp))
            Text("v0.1-alpha")
            Spacer(Modifier.height(20.dp))

            val data = snapshot
            if (data == null) {
                Text("Device telemetry: waiting")
            } else {
                val usedMemory = data.memoryTotalMb - data.memoryAvailableMb
                val memoryPercent = if (data.memoryTotalMb > 0) {
                    usedMemory * 100 / data.memoryTotalMb
                } else 0
                val storagePercent = if (data.storageTotalBytes > 0) {
                    data.storageFreeBytes * 100 / data.storageTotalBytes
                } else 0

                Text("RAM used: $memoryPercent%")
                Text("RAM available: ${data.memoryAvailableMb} MB")
                Text("Battery: ${data.batteryPercent}%")
                Text("Battery temperature: ${data.batteryTemperatureC?.let { "%.1f°C".format(it) } ?: "N/A"}")
                Text("Storage free: $storagePercent%")
                Text("Thermal status: ${thermalLabel(data.thermalStatus)}")
                Text("CPU telemetry: LIMITED (v0.1)")
            }

            Spacer(Modifier.height(20.dp))
            Text(if (monitoring) "● MONITORING ACTIVE" else "○ MONITORING OFF")
            Spacer(Modifier.height(20.dp))

            Button(onClick = { monitoring = !monitoring }) {
                Text(if (monitoring) "STOP" else "START ADAPTIVE")
            }
        }
    }
}

private fun thermalLabel(status: Int?): String = when (status) {
    null -> "UNAVAILABLE"
    0 -> "NONE"
    1 -> "LIGHT"
    2 -> "MODERATE"
    3 -> "SEVERE"
    4 -> "CRITICAL"
    5 -> "EMERGENCY"
    6 -> "SHUTDOWN"
    else -> "UNKNOWN"
}
