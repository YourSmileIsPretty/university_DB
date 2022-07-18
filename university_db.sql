--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1
-- Dumped by pg_dump version 13.1

-- Started on 2021-03-09 12:43:27

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 211 (class 1259 OID 17100)
-- Name: assessments_1semestr; Type: TABLE; Schema: public; Owner: university
--

CREATE TABLE public.assessments_1semestr (
    id integer NOT NULL,
    assessment integer NOT NULL,
    id_student integer,
    id_subject_1s integer
);


ALTER TABLE public.assessments_1semestr OWNER TO university;

--
-- TOC entry 210 (class 1259 OID 17098)
-- Name: assessments_1semestr_id_seq; Type: SEQUENCE; Schema: public; Owner: university
--

CREATE SEQUENCE public.assessments_1semestr_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.assessments_1semestr_id_seq OWNER TO university;

--
-- TOC entry 3067 (class 0 OID 0)
-- Dependencies: 210
-- Name: assessments_1semestr_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: university
--

ALTER SEQUENCE public.assessments_1semestr_id_seq OWNED BY public.assessments_1semestr.id;


--
-- TOC entry 213 (class 1259 OID 17118)
-- Name: assessments_2semestr; Type: TABLE; Schema: public; Owner: university
--

CREATE TABLE public.assessments_2semestr (
    id integer NOT NULL,
    assessment integer NOT NULL,
    id_student integer,
    id_subject_2s integer
);


ALTER TABLE public.assessments_2semestr OWNER TO university;

--
-- TOC entry 212 (class 1259 OID 17116)
-- Name: assessments_2semestr_id_seq; Type: SEQUENCE; Schema: public; Owner: university
--

CREATE SEQUENCE public.assessments_2semestr_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.assessments_2semestr_id_seq OWNER TO university;

--
-- TOC entry 3068 (class 0 OID 0)
-- Dependencies: 212
-- Name: assessments_2semestr_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: university
--

ALTER SEQUENCE public.assessments_2semestr_id_seq OWNED BY public.assessments_2semestr.id;


--
-- TOC entry 201 (class 1259 OID 17035)
-- Name: students; Type: TABLE; Schema: public; Owner: university
--

CREATE TABLE public.students (
    id integer NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.students OWNER TO university;

--
-- TOC entry 200 (class 1259 OID 17033)
-- Name: students_id_seq; Type: SEQUENCE; Schema: public; Owner: university
--

CREATE SEQUENCE public.students_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.students_id_seq OWNER TO university;

--
-- TOC entry 3069 (class 0 OID 0)
-- Dependencies: 200
-- Name: students_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: university
--

ALTER SEQUENCE public.students_id_seq OWNED BY public.students.id;


--
-- TOC entry 203 (class 1259 OID 17046)
-- Name: subjects_1semestr; Type: TABLE; Schema: public; Owner: university
--

CREATE TABLE public.subjects_1semestr (
    id integer NOT NULL,
    title text NOT NULL
);


ALTER TABLE public.subjects_1semestr OWNER TO university;

--
-- TOC entry 202 (class 1259 OID 17044)
-- Name: subjects_1semestr_id_seq; Type: SEQUENCE; Schema: public; Owner: university
--

CREATE SEQUENCE public.subjects_1semestr_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.subjects_1semestr_id_seq OWNER TO university;

--
-- TOC entry 3070 (class 0 OID 0)
-- Dependencies: 202
-- Name: subjects_1semestr_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: university
--

ALTER SEQUENCE public.subjects_1semestr_id_seq OWNED BY public.subjects_1semestr.id;


--
-- TOC entry 205 (class 1259 OID 17057)
-- Name: subjects_2semestr; Type: TABLE; Schema: public; Owner: university
--

CREATE TABLE public.subjects_2semestr (
    id integer NOT NULL,
    title text NOT NULL
);


ALTER TABLE public.subjects_2semestr OWNER TO university;

--
-- TOC entry 204 (class 1259 OID 17055)
-- Name: subjects_2semestr_id_seq; Type: SEQUENCE; Schema: public; Owner: university
--

CREATE SEQUENCE public.subjects_2semestr_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.subjects_2semestr_id_seq OWNER TO university;

--
-- TOC entry 3071 (class 0 OID 0)
-- Dependencies: 204
-- Name: subjects_2semestr_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: university
--

ALTER SEQUENCE public.subjects_2semestr_id_seq OWNED BY public.subjects_2semestr.id;


--
-- TOC entry 207 (class 1259 OID 17068)
-- Name: teachers_1semestr; Type: TABLE; Schema: public; Owner: university
--

CREATE TABLE public.teachers_1semestr (
    id integer NOT NULL,
    name text NOT NULL,
    id_subject_1s integer
);


ALTER TABLE public.teachers_1semestr OWNER TO university;

--
-- TOC entry 206 (class 1259 OID 17066)
-- Name: teachers_1semestr_id_seq; Type: SEQUENCE; Schema: public; Owner: university
--

CREATE SEQUENCE public.teachers_1semestr_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.teachers_1semestr_id_seq OWNER TO university;

--
-- TOC entry 3072 (class 0 OID 0)
-- Dependencies: 206
-- Name: teachers_1semestr_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: university
--

ALTER SEQUENCE public.teachers_1semestr_id_seq OWNED BY public.teachers_1semestr.id;


--
-- TOC entry 209 (class 1259 OID 17084)
-- Name: teachers_2semestr; Type: TABLE; Schema: public; Owner: university
--

CREATE TABLE public.teachers_2semestr (
    id integer NOT NULL,
    name text NOT NULL,
    id_subject_2s integer
);


ALTER TABLE public.teachers_2semestr OWNER TO university;

--
-- TOC entry 208 (class 1259 OID 17082)
-- Name: teachers_2semestr_id_seq; Type: SEQUENCE; Schema: public; Owner: university
--

CREATE SEQUENCE public.teachers_2semestr_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.teachers_2semestr_id_seq OWNER TO university;

--
-- TOC entry 3073 (class 0 OID 0)
-- Dependencies: 208
-- Name: teachers_2semestr_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: university
--

ALTER SEQUENCE public.teachers_2semestr_id_seq OWNED BY public.teachers_2semestr.id;


--
-- TOC entry 2896 (class 2604 OID 17103)
-- Name: assessments_1semestr id; Type: DEFAULT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.assessments_1semestr ALTER COLUMN id SET DEFAULT nextval('public.assessments_1semestr_id_seq'::regclass);


--
-- TOC entry 2897 (class 2604 OID 17121)
-- Name: assessments_2semestr id; Type: DEFAULT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.assessments_2semestr ALTER COLUMN id SET DEFAULT nextval('public.assessments_2semestr_id_seq'::regclass);


--
-- TOC entry 2891 (class 2604 OID 17038)
-- Name: students id; Type: DEFAULT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.students ALTER COLUMN id SET DEFAULT nextval('public.students_id_seq'::regclass);


--
-- TOC entry 2892 (class 2604 OID 17049)
-- Name: subjects_1semestr id; Type: DEFAULT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.subjects_1semestr ALTER COLUMN id SET DEFAULT nextval('public.subjects_1semestr_id_seq'::regclass);


--
-- TOC entry 2893 (class 2604 OID 17060)
-- Name: subjects_2semestr id; Type: DEFAULT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.subjects_2semestr ALTER COLUMN id SET DEFAULT nextval('public.subjects_2semestr_id_seq'::regclass);


--
-- TOC entry 2894 (class 2604 OID 17071)
-- Name: teachers_1semestr id; Type: DEFAULT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.teachers_1semestr ALTER COLUMN id SET DEFAULT nextval('public.teachers_1semestr_id_seq'::regclass);


--
-- TOC entry 2895 (class 2604 OID 17087)
-- Name: teachers_2semestr id; Type: DEFAULT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.teachers_2semestr ALTER COLUMN id SET DEFAULT nextval('public.teachers_2semestr_id_seq'::regclass);


--
-- TOC entry 3059 (class 0 OID 17100)
-- Dependencies: 211
-- Data for Name: assessments_1semestr; Type: TABLE DATA; Schema: public; Owner: university
--



--
-- TOC entry 3061 (class 0 OID 17118)
-- Dependencies: 213
-- Data for Name: assessments_2semestr; Type: TABLE DATA; Schema: public; Owner: university
--



--
-- TOC entry 3049 (class 0 OID 17035)
-- Dependencies: 201
-- Data for Name: students; Type: TABLE DATA; Schema: public; Owner: university
--



--
-- TOC entry 3051 (class 0 OID 17046)
-- Dependencies: 203
-- Data for Name: subjects_1semestr; Type: TABLE DATA; Schema: public; Owner: university
--



--
-- TOC entry 3053 (class 0 OID 17057)
-- Dependencies: 205
-- Data for Name: subjects_2semestr; Type: TABLE DATA; Schema: public; Owner: university
--



--
-- TOC entry 3055 (class 0 OID 17068)
-- Dependencies: 207
-- Data for Name: teachers_1semestr; Type: TABLE DATA; Schema: public; Owner: university
--



--
-- TOC entry 3057 (class 0 OID 17084)
-- Dependencies: 209
-- Data for Name: teachers_2semestr; Type: TABLE DATA; Schema: public; Owner: university
--



--
-- TOC entry 3074 (class 0 OID 0)
-- Dependencies: 210
-- Name: assessments_1semestr_id_seq; Type: SEQUENCE SET; Schema: public; Owner: university
--

SELECT pg_catalog.setval('public.assessments_1semestr_id_seq', 1, false);


--
-- TOC entry 3075 (class 0 OID 0)
-- Dependencies: 212
-- Name: assessments_2semestr_id_seq; Type: SEQUENCE SET; Schema: public; Owner: university
--

SELECT pg_catalog.setval('public.assessments_2semestr_id_seq', 1, false);


--
-- TOC entry 3076 (class 0 OID 0)
-- Dependencies: 200
-- Name: students_id_seq; Type: SEQUENCE SET; Schema: public; Owner: university
--

SELECT pg_catalog.setval('public.students_id_seq', 1, false);


--
-- TOC entry 3077 (class 0 OID 0)
-- Dependencies: 202
-- Name: subjects_1semestr_id_seq; Type: SEQUENCE SET; Schema: public; Owner: university
--

SELECT pg_catalog.setval('public.subjects_1semestr_id_seq', 1, false);


--
-- TOC entry 3078 (class 0 OID 0)
-- Dependencies: 204
-- Name: subjects_2semestr_id_seq; Type: SEQUENCE SET; Schema: public; Owner: university
--

SELECT pg_catalog.setval('public.subjects_2semestr_id_seq', 1, false);


--
-- TOC entry 3079 (class 0 OID 0)
-- Dependencies: 206
-- Name: teachers_1semestr_id_seq; Type: SEQUENCE SET; Schema: public; Owner: university
--

SELECT pg_catalog.setval('public.teachers_1semestr_id_seq', 1, false);


--
-- TOC entry 3080 (class 0 OID 0)
-- Dependencies: 208
-- Name: teachers_2semestr_id_seq; Type: SEQUENCE SET; Schema: public; Owner: university
--

SELECT pg_catalog.setval('public.teachers_2semestr_id_seq', 1, false);


--
-- TOC entry 2909 (class 2606 OID 17105)
-- Name: assessments_1semestr assessments_1semestr_pkey; Type: CONSTRAINT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.assessments_1semestr
    ADD CONSTRAINT assessments_1semestr_pkey PRIMARY KEY (id);


--
-- TOC entry 2911 (class 2606 OID 17123)
-- Name: assessments_2semestr assessments_2semestr_pkey; Type: CONSTRAINT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.assessments_2semestr
    ADD CONSTRAINT assessments_2semestr_pkey PRIMARY KEY (id);


--
-- TOC entry 2899 (class 2606 OID 17043)
-- Name: students students_pkey; Type: CONSTRAINT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (id);


--
-- TOC entry 2901 (class 2606 OID 17054)
-- Name: subjects_1semestr subjects_1semestr_pkey; Type: CONSTRAINT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.subjects_1semestr
    ADD CONSTRAINT subjects_1semestr_pkey PRIMARY KEY (id);


--
-- TOC entry 2903 (class 2606 OID 17065)
-- Name: subjects_2semestr subjects_2semestr_pkey; Type: CONSTRAINT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.subjects_2semestr
    ADD CONSTRAINT subjects_2semestr_pkey PRIMARY KEY (id);


--
-- TOC entry 2905 (class 2606 OID 17076)
-- Name: teachers_1semestr teachers_1semestr_pkey; Type: CONSTRAINT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.teachers_1semestr
    ADD CONSTRAINT teachers_1semestr_pkey PRIMARY KEY (id);


--
-- TOC entry 2907 (class 2606 OID 17092)
-- Name: teachers_2semestr teachers_2semestr_pkey; Type: CONSTRAINT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.teachers_2semestr
    ADD CONSTRAINT teachers_2semestr_pkey PRIMARY KEY (id);


--
-- TOC entry 2914 (class 2606 OID 17106)
-- Name: assessments_1semestr assessments_1semestr_id_student_fkey; Type: FK CONSTRAINT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.assessments_1semestr
    ADD CONSTRAINT assessments_1semestr_id_student_fkey FOREIGN KEY (id_student) REFERENCES public.students(id);


--
-- TOC entry 2915 (class 2606 OID 17111)
-- Name: assessments_1semestr assessments_1semestr_id_subject_1s_fkey; Type: FK CONSTRAINT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.assessments_1semestr
    ADD CONSTRAINT assessments_1semestr_id_subject_1s_fkey FOREIGN KEY (id_subject_1s) REFERENCES public.subjects_1semestr(id);


--
-- TOC entry 2916 (class 2606 OID 17124)
-- Name: assessments_2semestr assessments_2semestr_id_student_fkey; Type: FK CONSTRAINT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.assessments_2semestr
    ADD CONSTRAINT assessments_2semestr_id_student_fkey FOREIGN KEY (id_student) REFERENCES public.students(id);


--
-- TOC entry 2917 (class 2606 OID 17129)
-- Name: assessments_2semestr assessments_2semestr_id_subject_2s_fkey; Type: FK CONSTRAINT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.assessments_2semestr
    ADD CONSTRAINT assessments_2semestr_id_subject_2s_fkey FOREIGN KEY (id_subject_2s) REFERENCES public.subjects_2semestr(id);


--
-- TOC entry 2912 (class 2606 OID 17077)
-- Name: teachers_1semestr teachers_1semestr_id_subject_1s_fkey; Type: FK CONSTRAINT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.teachers_1semestr
    ADD CONSTRAINT teachers_1semestr_id_subject_1s_fkey FOREIGN KEY (id_subject_1s) REFERENCES public.subjects_1semestr(id);


--
-- TOC entry 2913 (class 2606 OID 17093)
-- Name: teachers_2semestr teachers_2semestr_id_subject_2s_fkey; Type: FK CONSTRAINT; Schema: public; Owner: university
--

ALTER TABLE ONLY public.teachers_2semestr
    ADD CONSTRAINT teachers_2semestr_id_subject_2s_fkey FOREIGN KEY (id_subject_2s) REFERENCES public.subjects_2semestr(id);


-- Completed on 2021-03-09 12:43:27

--
-- PostgreSQL database dump complete
--

