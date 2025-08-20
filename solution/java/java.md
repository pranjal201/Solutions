# 🏗️ Java Production-Ready Roadmap (12 Weeks)

A progressive, assignment-based roadmap to learn **Java for production-level development**.  
Each week has **goals, assignments, deliverables, acceptance criteria, and stretch tasks**.

---

## 📅 Week 1 — Core Java & OOP Foundations
**Goal:** Clean OOP design, error-proof code, CLI confidence.  

**Assignments:**
1. **BankAccount v1 (CLI)**  
   - deposit / withdraw / transfer  
   - handle edge cases: negative/zero amounts, insufficient funds, currency formatting  
2. **Employee hierarchy** (`Employee`, `Manager`, `Developer`) with overridden `getCompensation()`, `toString()`, `equals()/hashCode()`

**Deliverables:**  
- `bank-v1/` CLI app  
- `employee-model/` library (JAR)  

**Acceptance:**  
- No unchecked NPEs  
- Proper encapsulation  
- Unit tests for core methods (≥70% line coverage)  

**Stretch:**  
- Implement `Comparable<Employee>` + sorting with custom `Comparator`s  

---

## 📅 Week 2 — Exceptions, I/O, and Serialization
**Goal:** Robust error handling and clean resource management.  

**Assignments:**
1. **CSV/JSON Importer** for employees (add/update).  
   - Custom exceptions: `FileFormatException`, `DataMissingException`  
   - Use **try-with-resources**  
2. **Serialization demo** for `User` with versioned schema (`serialVersionUID`) and backward compatibility  

**Deliverables:**  
- `data-importer/` module with CLI: `--file employees.csv|json`  

**Acceptance:**  
- Clear error messages & exit codes  
- Temp files auto-deleted  
- ≥10 tests incl. failure paths  

**Stretch:**  
- Use NIO `Files.walk()` to bulk-load directory + parallelize with `ForkJoinPool`  

---

## 📅 Week 3 — Collections, Generics & Caching
**Goal:** Master collections performance & generics.  

**Assignments:**
1. **Student Manager** using `List`, `Set`, `Map`  
2. **LRU Cache** with `LinkedHashMap` + thread-safe wrapper  
3. **Generic Box<T>** with bounded types & wildcards  

**Deliverables:**  
- `collections-lab/` with JMH microbenchmarks  

**Acceptance:**  
- JMH report with observations  
- No concurrent modification issues  

**Stretch:**  
- Compare your cache with Guava or Caffeine  

---

## 📅 Week 4 — Concurrency & Multithreading
**Goal:** Correct + observable concurrent behavior.  

**Assignments:**
1. **Producer–Consumer** with `BlockingQueue`  
2. **Web Crawler Simulation** with thread pool, dedup, timeout  
3. **Alternating Printers** (three threads printing 1/2/3 in order)  

**Deliverables:**  
- `concurrency-lab/` with structured logs & metrics  

**Acceptance:**  
- No deadlocks  
- Proper `ThreadFactory` naming  
- Race condition tests with `CountDownLatch`  

**Stretch:**  
- Replace `synchronized` with `StampedLock` & compare perf  

---

## 📅 Week 5 — JDBC, SQL & DAO Pattern
**Goal:** Clean DB access with pooling and transactions.  

**Assignments:**
1. **UserDAO** CRUD with JDBC + HikariCP  
2. Transaction demo: transfer money between accounts (ACID)  
3. Pagination & filtering queries with `EXPLAIN`  

**Deliverables:**  
- `db-access/` module + `docker-compose.yml` for Postgres  

**Acceptance:**  
- No resource leaks  
- Pool metrics exposed  
- Integration tests with Testcontainers  

**Stretch:**  
- Batch inserts vs single inserts benchmark  

---

## 📅 Week 6 — Spring Boot: REST API
**Goal:** Production-ready service skeleton.  

**Assignments:**
1. **Employee Service API**: CRUD endpoints  
2. Layered architecture (Controller → Service → Repository)  
3. Global exception handler + validation (`@Valid`)  

**Deliverables:**  
- `employee-service/` Spring Boot app + OpenAPI docs  

**Acceptance:**  
- 100% API documented  
- Localized validation messages  
- Integration tests with `MockMvc`  

**Stretch:**  
- Add HATEOAS links or JSON:API compliance  

---

## 📅 Week 7 — Testing Strategy
**Goal:** Trustworthy change with safety nets.  

**Assignments:**
1. **Unit tests** (JUnit5 + Mockito)  
2. **Integration tests** with Testcontainers  
3. **Contract tests** with Pact or Spring Cloud Contract  

**Deliverables:**  
- `testing/` with coverage reports (JaCoCo)  

**Acceptance:**  
- ≥80% coverage service layer  
- Stable, non-flaky tests  

**Stretch:**  
- Property-based tests with jqwik  

---

## 📅 Week 8 — Security & Config
**Goal:** Secure by default.  

**Assignments:**
1. **JWT Authentication** with roles (`ADMIN`, `USER`)  
2. Method-level security (`@PreAuthorize`)  
3. Profiles: `dev`, `prod` + env-based secrets  

**Deliverables:**  
- `security/` module + Postman collection  

**Acceptance:**  
- Passwords hashed (BCrypt)  
- Token expiry & refresh  
- Security tests included  

**Stretch:**  
- OAuth2 login (Google) or Keycloak integration  

---

## 📅 Week 9 — Observability
**Goal:** Operate & debug in prod.  

**Assignments:**
1. Structured logging with MDC (requestId, userId)  
2. Micrometer + Prometheus metrics + Grafana dashboard  
3. OpenTelemetry tracing  

**Deliverables:**  
- `observability/` with docker compose for Prometheus + Grafana  

**Acceptance:**  
- P99 latency visible  
- Traces show DB calls  
- Logs carry correlation id  

**Stretch:**  
- Alerts for error rate / latency SLOs  

---

## 📅 Week 10 — Performance, Caching & Resilience
**Goal:** Make it fast & fault-tolerant.  

**Assignments:**
1. Add caching (Caffeine/Redis) with TTLs  
2. Resilience4j retry + circuit breaker + bulkhead  
3. Load test with k6 or Gatling  

**Deliverables:**  
- `perf/` with scripts & reports  

**Acceptance:**  
- ≥3× speedup on cached endpoints  
- No cache stampede  
- Load-test numbers recorded  

**Stretch:**  
- Async endpoints with `@Async` or Reactor  

---

## 📅 Week 11 — CI/CD & Deployment
**Goal:** Reproducible builds + automated pipelines.  

**Assignments:**
1. GitHub Actions: build → test → coverage → Docker image  
2. Containerize app (distroless base, probes)  
3. Deploy with Docker Compose stack  

**Deliverables:**  
- `.github/workflows/ci.yml`, `Dockerfile`, `compose.yaml`  

**Acceptance:**  
- Coverage <80% fails pipeline  
- Image passes security scan  
- Health checks work  

**Stretch:**  
- Helm chart + Kubernetes manifests  

---

## 📅 Week 12 — Capstone: Mini-LMS
**Goal:** Realistic service combining all concepts.  

**Features:**
- Domain: Users, Courses, Enrollments, Lessons, Progress  
- API: CRUD + enroll/unenroll, my courses, progress update  
- Auth: JWT with roles (ADMIN, USER)  
- DB: Postgres + Flyway migrations  
- Ops: Observability, caching, resilience, CI/CD  

**Deliverables:**  
- `lms-service/` with full README + setup guide  

**Acceptance:**  
- End-to-end Postman collection green  
- k6 load test report attached  
- Grafana dashboard + trace screenshot  

**Stretch:**  
- Event-driven email notifications (outbox pattern)  
- File uploads with pre-signed URLs  

---

## 📂 Standard Repo Layout