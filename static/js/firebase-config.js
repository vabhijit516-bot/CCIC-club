// Firebase Web SDK Configuration for CCIC AIML Club Portal
// Replace the placeholder values below with your Firebase Project Configuration from the Firebase Console:
// (Project Settings > General > Your apps > Web app > SDK setup and configuration)

const firebaseConfig = {
    apiKey: "AIzaSy_YOUR_FIREBASE_API_KEY_HERE",
    authDomain: "ccic-sairam-portal.firebaseapp.com",
    projectId: "ccic-sairam-portal",
    storageBucket: "ccic-sairam-portal.appspot.com",
    messagingSenderId: "123456789012",
    appId: "1:123456789012:web:abcdef1234567890"
};

// Designated list of Admin emails (synchronized with backend config)
const ADMIN_EMAILS = [
    "admin@sairam.edu.in",
    "ccic.aiml@sairam.edu.in",
    "admin@ccic.org",
    "coordinator@sairam.edu.in",
    "abhijit@sairam.edu.in"
];

// Check if actual Firebase keys have been configured or if running in Development/Demo mode
const isFirebaseConfigured = !firebaseConfig.apiKey.includes("YOUR_FIREBASE_API_KEY");

// Export configuration
window.CCIC_FIREBASE = {
    config: firebaseConfig,
    adminEmails: ADMIN_EMAILS,
    isConfigured: isFirebaseConfigured
};
