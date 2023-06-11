import axios from "axios";
import { BE_PATHS } from "../constants/paths";

export class WritingService {
  static async post(question, answer) {
    const url = `${import.meta.env.VITE_REACT_APP_BE_API_URL}/${
      BE_PATHS.WRITING
    }`;
    return await axios.post(url, {
      question,
      answer,
    });
  }
}
