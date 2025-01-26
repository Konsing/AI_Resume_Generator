import axios from "axios";

const API_URL = "http://127.0.0.1:5000/api/analyze"; // Flask backend URL

export const analyzeResume = async (resume, job) => {
  try {
    const response = await axios.post(API_URL, { resume, job });
    return response.data;
  } catch (error) {
    console.error("Error calling Flask API:", error);
    return { error: "Failed to fetch analysis" };
  }
};
