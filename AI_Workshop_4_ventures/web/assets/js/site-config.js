window.siteConfig = Object.assign(
  {
    formEndpoint: "",
    formServiceName: "Local workbook only",
    surveyPlatformName: "Google Forms",
    preEventSurveyUrl: "",
    feedbackSurveyUrl: "",
    surveyStatusLabel: "Survey status",
    surveyStatusValue: "Organizer-owned Google Forms are the canonical survey path. Public URLs are not stored in this repository.",
    volunteerContactLabel: "Organizer contact",
    volunteerContactValue: "Use the event communication channel shared by your unit leaders or presenter.",
    submissionInboxLabel: "Workbook storage",
    submissionInboxValue: "Participant workbook notes stay in this browser unless the learner chooses to print or download them.",
    submissionInboxUrl: "",
    responseSheetLabel: "Form response handling",
    responseSheetValue: "Canonical form handling is Google Forms to Google Sheets. Live organizer-owned form links are managed outside the public repo.",
    responseSheetUrl: "",
    responseSheetCsvUrl: ""
  },
  window.siteConfig || {}
);
