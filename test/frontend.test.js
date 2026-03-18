import { render, screen } from "@testing-library/react";
import App from "../frontend/src/App";

test("renders dashboard title", () => {
  render(<App />);
  const titleElement = screen.getByText(/Ransomware & Data Leak Dashboard/i);
  expect(titleElement).toBeInTheDocument();
});
