```mermaid
flowchart TD
    A[Start] --> Rand[Chose a random question]
    Rand --> B{Is the answer correct?}
    B -- Yes --> C[Add 1 life]
    B -- No --> D[Subtract 1 life]
    C --> E[Next question]
    D --> E[Next question]
    E --> Rand[Chose a random question]
    E --> F[End]
