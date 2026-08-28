# JD7 AI Adaptive v0.1-alpha

Initial Android project scaffold for the JD7 Adaptive device-stability system.

## Identity
- Application ID: `com.jd7.aiadaptive`
- Target SDK: 36 (Android 16 / Google Play baseline)
- Compile SDK: 37 (required by current Compose 1.12)
- Minimum SDK: 26
- Build system: Android Gradle Plugin 9.3.x
- UI: Jetpack Compose

## Current scope
- Initial launcher activity
- Compose dashboard
- Start/stop monitoring UI state
- Android application entry point

## Next implementation layers
1. Device telemetry
2. Health/Risk engines
3. Room persistence
4. Hilt dependency injection
5. WorkManager background scheduling
6. Self-monitoring and adaptive protection
7. Diagnostics and permission flow
8. Release signing and Google Play preparation

This branch is intentionally a development scaffold. No claim of APK build verification is made until the project is synced and built in Android Studio/Gradle.
