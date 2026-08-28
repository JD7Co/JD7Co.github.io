package com.jd7.aiadaptive

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            JD7Dashboard()
        }
    }
}

@Composable
private fun JD7Dashboard() {
    var monitoring by remember { mutableStateOf(false) }

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
            Spacer(Modifier.height(16.dp))
            Text("v0.1-alpha")
            Spacer(Modifier.height(24.dp))
            Text("Health: 100")
            Text("Risk: 0")
            Text(if (monitoring) "● MONITORING ACTIVE" else "○ MONITORING OFF")
            Spacer(Modifier.height(24.dp))
            Button(onClick = { monitoring = !monitoring }) {
                Text(if (monitoring) "STOP" else "START ADAPTIVE")
            }
        }
    }
}
