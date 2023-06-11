import { useState } from "react";
import { WritingService } from "../../services/writing";

export function Homepage() {
  const [loading, setLoading] = useState(false);
  const [question, setQuestion] = useState();
  const [essay, setEssay] = useState();
  const [reviews, setReviews] = useState(null);

  const onSubmit = async () => {
    if (question && essay) {
      setLoading(true);
      setReviews(null);
      const response = await WritingService.post(question, essay);
      setReviews(response?.data?.data);
      setLoading(false);
    }
  };

  return (
    <div className="horizontally-centered">
      <h1>IELTS Writing Digital Assistant</h1>
      <h3> Question: </h3>
      <textarea
        className="question-textarea"
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Input question here"
      ></textarea>
      <h3> Essay: </h3>
      <textarea
        className="essay-textarea"
        onChange={(e) => setEssay(e.target.value)}
        placeholder="Input your writing here"
      />
      <br />
      <button
        disabled={!(question && essay) || loading}
        onClick={() => onSubmit()}
        style={{ width: "100px", height: "30px" }}
      >
        Submit
      </button>
      <p>---</p>
      Task Response
      <textarea
        className="review-textarea"
        value={reviews?.task_response}
        disabled={!reviews || loading}
      />
      Coherence and Cohesion
      <textarea
        className="review-textarea"
        value={reviews?.coherence_and_cohesion}
        disabled={!reviews || loading}
      />
      Lexical Resource
      <textarea
        className="review-textarea"
        value={reviews?.lexical_resource}
        disabled={!reviews || loading}
      />
      Grammatical Range and Accuracy
      <textarea
        className="review-textarea"
        value={reviews?.grammatical_range_and_accuracy}
        disabled={!reviews || loading}
      />
      Overall Score
      <textarea
        className="review-textarea"
        value={reviews?.overall_score}
        disabled={!reviews || loading}
      />
    </div>
  );
}
