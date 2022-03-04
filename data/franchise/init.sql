--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

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

DROP DATABASE IF EXISTS franchise10;
--
-- Name: moma; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE franchise10 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE franchise10 OWNER TO postgres;

\connect franchise10

--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

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
-- Name: admins; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.admins (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    salary integer,
    work_position character varying(128) NOT NULL
);


ALTER TABLE public.admins OWNER TO postgres;

--
-- Name: admins_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.admins_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.admins_id_seq OWNER TO postgres;

--
-- Name: admins_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.admins_id_seq OWNED BY public.admins.id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: coaches; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.coaches (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    salary integer,
    work_position character varying(128) NOT NULL,
    team_id integer
);


ALTER TABLE public.coaches OWNER TO postgres;

--
-- Name: coaches_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.coaches_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.coaches_id_seq OWNER TO postgres;

--
-- Name: coaches_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.coaches_id_seq OWNED BY public.coaches.id;


--
-- Name: equipments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.equipments (
    id integer NOT NULL,
    helmet_size character varying(128) NOT NULL,
    shoulder_size character varying(128) NOT NULL,
    body_size character varying(128) NOT NULL,
    leg_size character varying(128) NOT NULL,
    player_id integer
);


ALTER TABLE public.equipments OWNER TO postgres;

--
-- Name: equipments_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.equipments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.equipments_id_seq OWNER TO postgres;

--
-- Name: equipments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.equipments_id_seq OWNED BY public.equipments.id;


--
-- Name: manages; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.manages (
    coach_id integer NOT NULL,
    player_id integer NOT NULL
);


ALTER TABLE public.manages OWNER TO postgres;

--
-- Name: players; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.players (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    salary integer,
    work_position character varying(128),
    status character varying(128) NOT NULL,
    experience character varying(128),
    team_id integer
);


ALTER TABLE public.players OWNER TO postgres;

--
-- Name: players_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.players_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.players_id_seq OWNER TO postgres;

--
-- Name: players_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.players_id_seq OWNED BY public.players.id;


--
-- Name: stadiums; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.stadiums (
    id integer NOT NULL,
    name character varying(128) NOT NULL,
    merchandise character varying(128),
    menu character varying(128),
    capacity integer NOT NULL
);


ALTER TABLE public.stadiums OWNER TO postgres;

--
-- Name: stadiums_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.stadiums_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.stadiums_id_seq OWNER TO postgres;

--
-- Name: stadiums_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.stadiums_id_seq OWNED BY public.stadiums.id;


--
-- Name: teams; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.teams (
    id integer NOT NULL,
    city character varying(128) NOT NULL,
    symbol character varying(128) NOT NULL,
    stadium_id integer,
    admin_id integer
);


ALTER TABLE public.teams OWNER TO postgres;

--
-- Name: teams_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.teams_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.teams_id_seq OWNER TO postgres;

--
-- Name: teams_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.teams_id_seq OWNED BY public.teams.id;


--
-- Name: admins id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admins ALTER COLUMN id SET DEFAULT nextval('public.admins_id_seq'::regclass);


--
-- Name: coaches id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.coaches ALTER COLUMN id SET DEFAULT nextval('public.coaches_id_seq'::regclass);


--
-- Name: equipments id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipments ALTER COLUMN id SET DEFAULT nextval('public.equipments_id_seq'::regclass);


--
-- Name: players id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.players ALTER COLUMN id SET DEFAULT nextval('public.players_id_seq'::regclass);


--
-- Name: stadiums id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stadiums ALTER COLUMN id SET DEFAULT nextval('public.stadiums_id_seq'::regclass);


--
-- Name: teams id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teams ALTER COLUMN id SET DEFAULT nextval('public.teams_id_seq'::regclass);


--
-- Data for Name: admins; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.admins (id, name, salary, work_position) FROM stdin;
11	Steve Keim	\N	GENERAL MANAGER
12	Richard W Cass	\N	PRESIDENT
13	Arthur Blank	\N	OWNER
14	Brandon Beane	\N	GENERAL MANAGER
15	Kevin King	\N	Head Athletic Trainer
16	Robert	\N	Kraft
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
9292a41e40c5
\.


--
-- Data for Name: coaches; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.coaches (id, name, salary, work_position, team_id) FROM stdin;
11	Jeff Rodgers	\N	SPECIAL TEAMS	14
12	Rob Ryan	\N	INSIDE LINEBACKERS COACH	15
13	Charles London	\N	QUARTERBACKS	16
14	Ryan Wendell	\N	ASSISTANT OFFENSIVE LINE	17
15	Brian Angelichio	\N	TIGHT ENDS	18
17	Bill	\N	Bellichek	\N
\.


--
-- Data for Name: equipments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.equipments (id, helmet_size, shoulder_size, body_size, leg_size, player_id) FROM stdin;
11	XL	L	XXL	L	11
12	L	XL	L	S	12
13	S	L	L	S	13
14	S	S	L	S	14
15	XL	XXL	XL	XL	15
17	XL	XXL	XXL	L	18
\.


--
-- Data for Name: manages; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.manages (coach_id, player_id) FROM stdin;
11	11
12	12
13	13
14	14
15	15
\.


--
-- Data for Name: players; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.players (id, name, salary, work_position, status, experience, team_id) FROM stdin;
11	Matt Prater	\N	K	Active	15 years	14
12	Chris Board	\N	LB	Active	4 years	15
13	MATT RYAN	\N	QB	Active	14 years	16
14	Ryan Bates	\N	G	Active	3 years	17
15	Stephen Sullivan Jr	\N	TE	Active	3 years	18
18	Kyler Murray	\N	QB	Active	2 years	14
19	Zach Allen	\N	DE	Active	3 years	14
20	Mark Andrews	\N	TE	Active	4 years	15
21	Josh Andrews	\N	OL	Active	6 years	16
22	Josh Allen	\N	QB	Active	3 years	17
23	Sam Darnold	\N	QB	Active	4 years	18
24	Pat Elflein	\N	G	Active	5 years	18
25	Tyler Bass	\N	K	Active	2 years	17
26	Frank Darby	\N	WR	Active	Rookie	16
27	Anthony Averett	\N	CB	Active	4 years	15
28	Budda Baker	\N	S	Active	5 years	14
\.


--
-- Data for Name: stadiums; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.stadiums (id, name, merchandise, menu, capacity) FROM stdin;
11	State Farm Stadium	\N	\N	63400
12	M and T Bank Stadium	\N	\N	67000
13	Mercedes Benz Stadium	\N	\N	71000
14	Highmark Stadium	\N	\N	71608
15	Bank of America Stadium	\N	\N	80000
16	Ford Field	\N	\N	65000
\.


--
-- Data for Name: teams; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.teams (id, city, symbol, stadium_id, admin_id) FROM stdin;
14	Arizona	Cardinals	11	11
15	Baltimore	Ravens	12	12
16	Atlanta	Falcons	13	13
17	Buffalo	Bills	14	14
18	Carolina	Panthers	15	15
31	Las Vegas	Raiders	\N	\N
30	Washington	Commanders	\N	\N
\.


--
-- Name: admins_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.admins_id_seq', 16, true);


--
-- Name: coaches_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.coaches_id_seq', 17, true);


--
-- Name: equipments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.equipments_id_seq', 17, true);


--
-- Name: players_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.players_id_seq', 28, true);


--
-- Name: stadiums_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.stadiums_id_seq', 16, true);


--
-- Name: teams_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.teams_id_seq', 31, true);


--
-- Name: admins admins_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admins
    ADD CONSTRAINT admins_name_key UNIQUE (name);


--
-- Name: admins admins_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admins
    ADD CONSTRAINT admins_pkey PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: coaches coaches_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.coaches
    ADD CONSTRAINT coaches_name_key UNIQUE (name);


--
-- Name: coaches coaches_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.coaches
    ADD CONSTRAINT coaches_pkey PRIMARY KEY (id);


--
-- Name: equipments equipments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipments
    ADD CONSTRAINT equipments_pkey PRIMARY KEY (id);


--
-- Name: manages manages_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manages
    ADD CONSTRAINT manages_pkey PRIMARY KEY (coach_id, player_id);


--
-- Name: players players_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.players
    ADD CONSTRAINT players_name_key UNIQUE (name);


--
-- Name: players players_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.players
    ADD CONSTRAINT players_pkey PRIMARY KEY (id);


--
-- Name: stadiums stadiums_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stadiums
    ADD CONSTRAINT stadiums_name_key UNIQUE (name);


--
-- Name: stadiums stadiums_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.stadiums
    ADD CONSTRAINT stadiums_pkey PRIMARY KEY (id);


--
-- Name: teams teams_city_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_city_key UNIQUE (city);


--
-- Name: teams teams_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_pkey PRIMARY KEY (id);


--
-- Name: players_btree_index; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX players_btree_index ON public.players USING btree (name);


--
-- Name: coaches coaches_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.coaches
    ADD CONSTRAINT coaches_team_id_fkey FOREIGN KEY (team_id) REFERENCES public.teams(id);


--
-- Name: equipments equipments_player_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipments
    ADD CONSTRAINT equipments_player_id_fkey FOREIGN KEY (player_id) REFERENCES public.players(id);


--
-- Name: manages manages_coach_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manages
    ADD CONSTRAINT manages_coach_id_fkey FOREIGN KEY (coach_id) REFERENCES public.coaches(id);


--
-- Name: manages manages_player_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manages
    ADD CONSTRAINT manages_player_id_fkey FOREIGN KEY (player_id) REFERENCES public.players(id);


--
-- Name: players players_team_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.players
    ADD CONSTRAINT players_team_id_fkey FOREIGN KEY (team_id) REFERENCES public.teams(id);


--
-- Name: teams teams_admin_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_admin_id_fkey FOREIGN KEY (admin_id) REFERENCES public.admins(id);


--
-- Name: teams teams_stadium_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teams
    ADD CONSTRAINT teams_stadium_id_fkey FOREIGN KEY (stadium_id) REFERENCES public.stadiums(id);


--
-- PostgreSQL database dump complete
--

