import React, { useState, useRef } from "react";
import "./App.css";
import SVGComponent from "./SVGComponent";

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);
  const [prediction, setPrediction] = useState("");
  const [confidence, setConfidence] = useState("");
  const [status, setStatus] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");
  const fileInputRef = useRef(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
    setError(""); // Clear error message when a file is selected

    // Create a URL for the image preview
    if (file) {
      setPreviewUrl(URL.createObjectURL(file));
    }
  };

  const handleCancel = () => {
    setSelectedFile(null);
    setPrediction("");
    setConfidence(""); // Clear confidence on cancel
    setStatus("");
    setError(""); // Clear error message on cancel

    // Revoke the object URL to free up memory
    if (previewUrl) {
      URL.revokeObjectURL(previewUrl);
    }
    setPreviewUrl(null);

    if (fileInputRef.current) {
      fileInputRef.current.value = null;
    }
  };

  // const handleSubmit = async (event) => {
  //   event.preventDefault();
  //   if (!selectedFile) {
  //     setError("No image selected!");
  //     return;
  //   }

  //   const formData = new FormData();
  //   formData.append("file", selectedFile);

  //   try {
  //     setIsLoading(true);
  //     setError("");
  //     const serverUrl =
  //       import.meta.env.MODE === "production"
  //         ? import.meta.env.VITE_API_PRODUCTION_URL
  //         : import.meta.env.VITE_API_DEVELOPMENT_URL;
  //     const response = await fetch(serverUrl, {
  //       method: "POST",
  //       body: formData,
  //     });

  //     if (!response.ok) {
  //       throw new Error("Network response was not ok");
  //     }

  //     const data = await response.json();
  //     setPrediction(data.class);
  //     setConfidence(data.confidence); // Set confidence percentage from response
  //     setStatus(data.status);
  //   } catch (error) {
  //     console.error("Error during prediction:", error);
  //     setStatus("Oops! Seems like this is not a skin image!");
  //     setConfidence(""); // Clear confidence if an error occurs
  //     setPrediction("");
  //   } finally {
  //     setIsLoading(false);
  //   }
  // };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!selectedFile) {
      setError("No image selected!");
      return;
    }
  
    const formData = new FormData();
    formData.append("file", selectedFile);
  
    try {
      setIsLoading(true);
      setError(""); // Clear any previous error messages
  
      const serverUrl =
        import.meta.env.MODE === "production"
          ? import.meta.env.VITE_API_PRODUCTION_URL
          : import.meta.env.VITE_API_DEVELOPMENT_URL;

        console.log("serverurl=",serverUrl);
  
      const response = await fetch(serverUrl, {
        method: "POST",
        body: formData,
        credentials: "include",
      });

      const data = await response.json();
      console.log(data);
  
      // Check if response is ok
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || "An error occurred while processing your request.");
      }
  
      // const data = await response.json();
      setPrediction(data.class);
      setConfidence(data.confidence);
      setStatus(data.status);
    } catch (error) {
      console.error("Error during prediction:", error);
      // Check if the error is due to network/server issues
      if (error.message.includes("NetworkError")) {
        setError("Server is currently unavailable. Please try again later.");
      } else {
        setStatus("Oops! Seems like this is not a skin image!");
        setConfidence(""); // Clear confidence if an error occurs
        setPrediction("");
      }
    } finally {
      setIsLoading(false);
    }
  };
  

  return (
    <div className="flex flex-col items-center bg-[#15202b] h-screen w-full">
      <h1 className="flex mt-8 mb-4 font-bold p-3 rounded-md text-white text-4xl max-md:text-2xl">
        Skin Cancer Type Detection
      </h1>
      <form
        onSubmit={handleSubmit}
        className="flex max-md:flex-col items-center space-x-4"
      >
        <input
          type="file"
          accept="image/*"
          onChange={handleFileChange}
          ref={fileInputRef}
          className="my-5 bg-sky-800 p-3 rounded-md shadow-md shadow-black text-white font-semibold"
        />
        <div className="space-x-3">
          {selectedFile && (
            <button
              type="button"
              onClick={handleCancel}
              className="p-3 bg-red-600 rounded-md text-white shadow-md shadow-black font-semibold"
            >
              Cancel
            </button>
          )}
          <button
            type="submit"
            className="p-3 bg-green-700 text-white rounded-md shadow-md shadow-black font-semibold"
          >
            Check
          </button>
        </div>
      </form>
      {previewUrl && (
        <img
          src={previewUrl}
          alt="Selected Preview"
          className="w-64 h-64 object-cover rounded-md shadow-md shadow-black mt-4"
        />
      )}

      {error && <div className="text-red-500 mt-2">{error}</div>}

      {status ? (
        <div className="mt-5 p-3 flex flex-col items-center min-w-64 text-xl font-semibold">
          <div
            className={`text-xl shadow-black shadow-md px-3 py-1 bg-slate-700 rounded-md ${
              status === "Benign" ? "text-green-500" : "text-red-600"
            }`}
          >
            {" "}
            {status}
          </div>
          {prediction && (
            <div className="mt-5 text-sm text-white">Class: {prediction}</div>
          )}
          {confidence && (
            <div className=" text-sm text-white">Confidence: {confidence}</div>
          )}
        </div>
      ) : isLoading ? (
        <div className="flex items-center mt-5">
          <div className="h-20 animate-up-down">
            <SVGComponent />
          </div>
          <div className="text-white">Please Wait...</div>
        </div>
      ) : selectedFile ? (
        <div className="mt-5 text-white">Click Check button</div>
      ) : (
        <div className="mt-5 text-white">
          Select an image and click "Check" for prediction
        </div>
      )}
    </div>
  );
}

export default App;
