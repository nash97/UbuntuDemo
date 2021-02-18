-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 05, 2021 at 11:24 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `presidencyonlineexaminations`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(3, 'Admin'),
(4, 'Guests'),
(1, 'Students'),
(2, 'Teachers');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add course plan model', 7, 'add_courseplanmodel'),
(26, 'Can change course plan model', 7, 'change_courseplanmodel'),
(27, 'Can delete course plan model', 7, 'delete_courseplanmodel'),
(28, 'Can view course plan model', 7, 'view_courseplanmodel'),
(29, 'Can add student result model', 8, 'add_studentresultmodel'),
(30, 'Can change student result model', 8, 'change_studentresultmodel'),
(31, 'Can delete student result model', 8, 'delete_studentresultmodel'),
(32, 'Can view student result model', 8, 'view_studentresultmodel'),
(33, 'Can add course reference model', 9, 'add_coursereferencemodel'),
(34, 'Can change course reference model', 9, 'change_coursereferencemodel'),
(35, 'Can delete course reference model', 9, 'delete_coursereferencemodel'),
(36, 'Can view course reference model', 9, 'view_coursereferencemodel'),
(37, 'Can add questions model', 10, 'add_questionsmodel'),
(38, 'Can change questions model', 10, 'change_questionsmodel'),
(39, 'Can delete questions model', 10, 'delete_questionsmodel'),
(40, 'Can view questions model', 10, 'view_questionsmodel'),
(41, 'Can add topics model', 11, 'add_topicsmodel'),
(42, 'Can change topics model', 11, 'change_topicsmodel'),
(43, 'Can delete topics model', 11, 'delete_topicsmodel'),
(44, 'Can view topics model', 11, 'view_topicsmodel'),
(45, 'Can add subscription details model', 12, 'add_subscriptiondetailsmodel'),
(46, 'Can change subscription details model', 12, 'change_subscriptiondetailsmodel'),
(47, 'Can delete subscription details model', 12, 'delete_subscriptiondetailsmodel'),
(48, 'Can view subscription details model', 12, 'view_subscriptiondetailsmodel'),
(49, 'Can add courses model', 13, 'add_coursesmodel'),
(50, 'Can change courses model', 13, 'change_coursesmodel'),
(51, 'Can delete courses model', 13, 'delete_coursesmodel'),
(52, 'Can view courses model', 13, 'view_coursesmodel'),
(53, 'Can add subscription model', 14, 'add_subscriptionmodel'),
(54, 'Can change subscription model', 14, 'change_subscriptionmodel'),
(55, 'Can delete subscription model', 14, 'delete_subscriptionmodel'),
(56, 'Can view subscription model', 14, 'view_subscriptionmodel'),
(57, 'Can add user registration model', 15, 'add_userregistrationmodel'),
(58, 'Can change user registration model', 15, 'change_userregistrationmodel'),
(59, 'Can delete user registration model', 15, 'delete_userregistrationmodel'),
(60, 'Can view user registration model', 15, 'view_userregistrationmodel'),
(61, 'Can add subjects model', 16, 'add_subjectsmodel'),
(62, 'Can change subjects model', 16, 'change_subjectsmodel'),
(63, 'Can delete subjects model', 16, 'delete_subjectsmodel'),
(64, 'Can view subjects model', 16, 'view_subjectsmodel'),
(65, 'Can add question types model', 17, 'add_questiontypesmodel'),
(66, 'Can change question types model', 17, 'change_questiontypesmodel'),
(67, 'Can delete question types model', 17, 'delete_questiontypesmodel'),
(68, 'Can view question types model', 17, 'view_questiontypesmodel'),
(69, 'Can add sub topics model', 18, 'add_subtopicsmodel'),
(70, 'Can change sub topics model', 18, 'change_subtopicsmodel'),
(71, 'Can delete sub topics model', 18, 'delete_subtopicsmodel'),
(72, 'Can view sub topics model', 18, 'view_subtopicsmodel'),
(73, 'Can add image questions model', 19, 'add_imagequestionsmodel'),
(74, 'Can change image questions model', 19, 'change_imagequestionsmodel'),
(75, 'Can delete image questions model', 19, 'delete_imagequestionsmodel'),
(76, 'Can view image questions model', 19, 'view_imagequestionsmodel'),
(77, 'Can add demo user registration model', 20, 'add_demouserregistrationmodel'),
(78, 'Can change demo user registration model', 20, 'change_demouserregistrationmodel'),
(79, 'Can delete demo user registration model', 20, 'delete_demouserregistrationmodel'),
(80, 'Can view demo user registration model', 20, 'view_demouserregistrationmodel');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$216000$ZbsuStvIW7nJ$PDxQxswccXlBBkvSeXC1t6u9dnX3EQPYlhtEm+tIosc=', '2021-02-04 04:29:49.373761', 1, 'akhil', '', '', 'akhil@mail.com', 1, 1, '2021-01-31 06:25:51.427930'),
(2, 'pbkdf2_sha256$216000$bBNI1RyKRUrE$NMUT+M5BSgU9KkkEnWNxrYER/iqa0v58w5J1987aw5E=', '2021-02-02 03:50:42.987312', 0, 'Karishma', '', '', 'karishma@mail.com', 1, 1, '2021-02-02 03:48:34.000000'),
(3, 'pbkdf2_sha256$216000$nTN9hvEjirfC$6TZjNQf/d11B9XgdRjSvrlsU7Q0pi1FD5fcRrZJgycs=', NULL, 0, 'Raj', '', '', 'raju@mail.com', 0, 1, '2021-02-02 03:49:24.000000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-02-01 04:40:03.735617', '2', 'JEE', 1, '[{\"added\": {}}]', 13, 1),
(2, '2021-02-01 04:40:21.464040', '1', 'Physics', 1, '[{\"added\": {}}]', 16, 1),
(3, '2021-02-01 04:40:36.106411', '1', 'Thermodynamics', 1, '[{\"added\": {}}]', 11, 1),
(4, '2021-02-01 04:40:53.401191', '1', 'Numerical', 1, '[{\"added\": {}}]', 17, 1),
(5, '2021-02-01 04:41:13.850932', '1', 'what is thermodynamics', 1, '[{\"added\": {}}]', 10, 1),
(6, '2021-02-01 04:41:27.559410', '1', 'TimeBased', 1, '[{\"added\": {}}]', 9, 1),
(7, '2021-02-01 04:41:44.066297', '1', '5 test papers', 1, '[{\"added\": {}}]', 7, 1),
(8, '2021-02-01 04:42:34.761585', '2', 'studentResultModel object (2)', 1, '[{\"added\": {}}]', 8, 1),
(9, '2021-02-01 06:21:45.856182', '2', 'subscriptionModel object (2)', 1, '[{\"added\": {}}]', 14, 1),
(10, '2021-02-01 06:22:29.846756', '1', 'Silver', 1, '[{\"added\": {}}]', 12, 1),
(11, '2021-02-01 11:09:31.896826', '2', 'Thermo1', 1, '[{\"added\": {}}]', 18, 1),
(12, '2021-02-01 11:10:11.110932', '2', 'Multiple MCQ', 1, '[{\"added\": {}}]', 17, 1),
(13, '2021-02-01 11:12:16.437520', '1', 'imageQuestionsModel object (1)', 1, '[{\"added\": {}}]', 19, 1),
(14, '2021-02-02 03:47:15.270632', '1', 'Students', 1, '[{\"added\": {}}]', 3, 1),
(15, '2021-02-02 03:47:28.481434', '2', 'Teachers', 1, '[{\"added\": {}}]', 3, 1),
(16, '2021-02-02 03:47:51.970240', '3', 'Admin', 1, '[{\"added\": {}}]', 3, 1),
(17, '2021-02-02 03:48:01.824444', '4', 'Guests', 1, '[{\"added\": {}}]', 3, 1),
(18, '2021-02-02 03:48:34.657391', '2', 'Karishma', 1, '[{\"added\": {}}]', 4, 1),
(19, '2021-02-02 03:48:57.856581', '2', 'Karishma', 2, '[{\"changed\": {\"fields\": [\"Staff status\", \"Groups\"]}}]', 4, 1),
(20, '2021-02-02 03:49:06.971711', '2', 'Karishma', 2, '[{\"changed\": {\"fields\": [\"Email address\"]}}]', 4, 1),
(21, '2021-02-02 03:49:24.589603', '3', 'Raj', 1, '[{\"added\": {}}]', 4, 1),
(22, '2021-02-02 03:49:31.052813', '3', 'Raj', 2, '[{\"changed\": {\"fields\": [\"Email address\"]}}]', 4, 1),
(23, '2021-02-02 07:05:10.003666', '3', 'Karishma', 3, '', 15, 1),
(24, '2021-02-02 07:05:10.008804', '2', 'Karishma', 3, '', 15, 1),
(25, '2021-02-02 07:05:10.013983', '1', 'Akhilesh', 3, '', 15, 1),
(26, '2021-02-03 10:41:52.465170', '1', 'Akhilesh', 1, '[{\"added\": {}}]', 20, 1),
(27, '2021-02-05 05:26:23.913404', '3', 'Payal', 1, '[{\"added\": {}}]', 20, 1),
(28, '2021-02-05 05:26:55.947011', '4', 'Nashit', 1, '[{\"added\": {}}]', 20, 1),
(29, '2021-02-05 10:10:58.623586', '11', 'coursesModel object (11)', 1, '[{\"added\": {}}]', 13, 1),
(30, '2021-02-05 10:11:12.312242', '11', 'coursesModel object (11)', 3, '', 13, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'studentexams', 'courseplanmodel'),
(9, 'studentexams', 'coursereferencemodel'),
(13, 'studentexams', 'coursesmodel'),
(20, 'studentexams', 'demouserregistrationmodel'),
(19, 'studentexams', 'imagequestionsmodel'),
(10, 'studentexams', 'questionsmodel'),
(17, 'studentexams', 'questiontypesmodel'),
(8, 'studentexams', 'studentresultmodel'),
(16, 'studentexams', 'subjectsmodel'),
(12, 'studentexams', 'subscriptiondetailsmodel'),
(14, 'studentexams', 'subscriptionmodel'),
(18, 'studentexams', 'subtopicsmodel'),
(11, 'studentexams', 'topicsmodel'),
(15, 'studentexams', 'userregistrationmodel');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-01-31 06:25:29.979584'),
(2, 'auth', '0001_initial', '2021-01-31 06:25:30.166483'),
(3, 'admin', '0001_initial', '2021-01-31 06:25:30.621127'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-01-31 06:25:30.728923'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-01-31 06:25:30.753761'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-01-31 06:25:30.820550'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-01-31 06:25:30.885412'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-01-31 06:25:30.906239'),
(9, 'auth', '0004_alter_user_username_opts', '2021-01-31 06:25:30.916684'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-01-31 06:25:30.958735'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-01-31 06:25:30.964197'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-01-31 06:25:30.970799'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-01-31 06:25:30.989366'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-01-31 06:25:31.005498'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-01-31 06:25:31.025368'),
(16, 'auth', '0011_update_proxy_permissions', '2021-01-31 06:25:31.034831'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-01-31 06:25:31.050968'),
(18, 'sessions', '0001_initial', '2021-01-31 06:25:31.074876'),
(19, 'studentexams', '0001_initial', '2021-01-31 14:49:16.152300'),
(20, 'studentexams', '0002_auto_20210201_1059', '2021-02-01 05:29:15.309840'),
(21, 'studentexams', '0002_auto_20210201_1136', '2021-02-01 06:06:51.883315'),
(22, 'studentexams', '0003_auto_20210201_1638', '2021-02-01 11:08:44.109083'),
(23, 'studentexams', '0002_auto_20210203_1237', '2021-02-03 07:07:09.174921');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('5th00htyaj2yu25wmtbgrzdbyo6oik2n', '.eJxVjssOgyAURP-FdUME5NVV477fYC5wUapiIrpq-u_FxEW7nTNzMm_Sw7GP_VFw61Mgd8LI7Tdz4CfMJwgvyMNK_Zr3LTl6VuhFC32uAefu6v4JRihjXQs0QlnGvOOmYRoBnTQyykagtg5QgYYIPhpmecu9cVYL1RphYwAuua9SXCDNVQXTlDYIRbaCs8dwpvXVQj5fA3FC1g:1l6uP5:Fx__yIBzX5MOgZvRXhXz03jYOI-o1a0z7KCk6ASND78', '2021-02-16 12:03:31.562600'),
('jazxbe25mz47rebodegu52jyl18ptbji', '.eJxVjssOgyAURP-FdUME5NVV477fYC5wUapiIrpq-u_FxEW7nTNzMm_Sw7GP_VFw61Mgd8LI7Tdz4CfMJwgvyMNK_Zr3LTl6VuhFC32uAefu6v4JRihjXQs0QlnGvOOmYRoBnTQyykagtg5QgYYIPhpmecu9cVYL1RphYwAuua9SXCDNVQXTlDYIRbaCs8dwpvXVQj5fA3FC1g:1l7bei:46UG3XTmFdBBza-DIsoIEsUiEXoBPx8_N0Z4kGxNUgc', '2021-02-18 10:14:32.977338');

-- --------------------------------------------------------

--
-- Table structure for table `imagequestionsmodel`
--

CREATE TABLE `imagequestionsmodel` (
  `id` int(11) NOT NULL,
  `imageQuestion` varchar(100) NOT NULL,
  `img1` varchar(100) NOT NULL,
  `img2` varchar(100) NOT NULL,
  `img3` varchar(100) NOT NULL,
  `img4` varchar(100) NOT NULL,
  `answer` varchar(19) NOT NULL,
  `marks` int(10) UNSIGNED NOT NULL CHECK (`marks` >= 0),
  `Complexity` varchar(50) DEFAULT NULL,
  `topic_id_id` int(11) DEFAULT NULL,
  `type_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `studentexams_courseplanmodel`
--

CREATE TABLE `studentexams_courseplanmodel` (
  `id` int(11) NOT NULL,
  `availableCourse` varchar(100) DEFAULT NULL,
  `attemptedCourse` varchar(100) DEFAULT NULL,
  `createdPlan` date NOT NULL,
  `updatedPlan` date NOT NULL,
  `status` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studentexams_courseplanmodel`
--

INSERT INTO `studentexams_courseplanmodel` (`id`, `availableCourse`, `attemptedCourse`, `createdPlan`, `updatedPlan`, `status`) VALUES
(1, '5 test papers', '5', '2021-02-01', '2021-02-01', 1);

-- --------------------------------------------------------

--
-- Table structure for table `studentexams_coursereferencemodel`
--

CREATE TABLE `studentexams_coursereferencemodel` (
  `id` int(11) NOT NULL,
  `courseType` varchar(100) DEFAULT NULL,
  `status` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studentexams_coursereferencemodel`
--

INSERT INTO `studentexams_coursereferencemodel` (`id`, `courseType`, `status`) VALUES
(1, 'TimeBased', 1);

-- --------------------------------------------------------

--
-- Table structure for table `studentexams_coursesmodel`
--

CREATE TABLE `studentexams_coursesmodel` (
  `id` int(11) NOT NULL,
  `courseName` varchar(100) DEFAULT NULL,
  `status` smallint(6) NOT NULL,
  `student_id_id` int(11) DEFAULT NULL,
  `extraCourse` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studentexams_coursesmodel`
--

INSERT INTO `studentexams_coursesmodel` (`id`, `courseName`, `status`, `student_id_id`, `extraCourse`) VALUES
(3, 'JEE Mains', 1, NULL, NULL),
(4, 'JEE Mains', 1, NULL, NULL),
(5, 'JEE Mains', 1, NULL, NULL),
(6, 'JEE Mains', 1, NULL, NULL),
(7, 'JEE Mains', 1, NULL, NULL),
(8, 'JEE Mains', 1, NULL, NULL),
(9, 'Courses', 1, NULL, NULL),
(10, 'Courses', 1, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `studentexams_demouserregistrationmodel`
--

CREATE TABLE `studentexams_demouserregistrationmodel` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `mobile` varchar(30) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `package` varchar(30) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studentexams_demouserregistrationmodel`
--

INSERT INTO `studentexams_demouserregistrationmodel` (`id`, `name`, `mobile`, `email`, `package`, `status`) VALUES
(1, 'Akhilesh', '9012316451', 'akhilesh@mail.com', 'Jee', 1),
(2, 'Karishma', '9012316451', 'karishma@mail.com', 'IEEE', 1),
(3, 'Payal', '9012316451', 'payal@mail.com', 'IEEE', 1),
(4, 'Nashit', '8965875498', 'nashit@mail.com', 'JEE Advanced', 1);

-- --------------------------------------------------------

--
-- Table structure for table `studentexams_questionsmodel`
--

CREATE TABLE `studentexams_questionsmodel` (
  `id` int(11) NOT NULL,
  `Question` varchar(1000) DEFAULT NULL,
  `c1` varchar(200) NOT NULL,
  `c2` varchar(200) NOT NULL,
  `c3` varchar(200) NOT NULL,
  `c4` varchar(200) NOT NULL,
  `marks` int(10) UNSIGNED NOT NULL CHECK (`marks` >= 0),
  `answer` varchar(11) NOT NULL,
  `topic_id_id` int(11) DEFAULT NULL,
  `type_id_id` int(11) DEFAULT NULL,
  `Complexity` varchar(50) DEFAULT NULL,
  `subTopic_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `studentexams_questiontypesmodel`
--

CREATE TABLE `studentexams_questiontypesmodel` (
  `id` int(11) NOT NULL,
  `questionType` varchar(200) DEFAULT NULL,
  `status` smallint(6) NOT NULL,
  `topics_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `studentexams_studentresultmodel`
--

CREATE TABLE `studentexams_studentresultmodel` (
  `id` int(11) NOT NULL,
  `marks` int(10) UNSIGNED DEFAULT NULL CHECK (`marks` >= 0),
  `exam_date` datetime(6) NOT NULL,
  `createdResult` date NOT NULL,
  `updatedResult` date NOT NULL,
  `status` smallint(6) NOT NULL,
  `student_id_id` int(11) DEFAULT NULL,
  `subject_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `studentexams_subjectsmodel`
--

CREATE TABLE `studentexams_subjectsmodel` (
  `id` int(11) NOT NULL,
  `subjectName` varchar(200) DEFAULT NULL,
  `status` smallint(6) NOT NULL,
  `course_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studentexams_subjectsmodel`
--

INSERT INTO `studentexams_subjectsmodel` (`id`, `subjectName`, `status`, `course_id_id`) VALUES
(2, 'Physics', 1, 8),
(3, 'Subjects', 1, 9),
(4, 'Subjects', 1, 10);

-- --------------------------------------------------------

--
-- Table structure for table `studentexams_subscriptiondetailsmodel`
--

CREATE TABLE `studentexams_subscriptiondetailsmodel` (
  `id` int(11) NOT NULL,
  `badges` varchar(100) DEFAULT NULL,
  `subscriptionStartDate` date NOT NULL,
  `subscriptionEndDate` date NOT NULL,
  `status` smallint(6) NOT NULL,
  `courseType_id` int(11) DEFAULT NULL,
  `userId_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `studentexams_subscriptionmodel`
--

CREATE TABLE `studentexams_subscriptionmodel` (
  `id` int(11) NOT NULL,
  `createdDate` datetime(6) NOT NULL,
  `deletedDate` datetime(6) NOT NULL,
  `status` smallint(6) NOT NULL,
  `courseType_id` int(11) DEFAULT NULL,
  `userId_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `studentexams_subtopicsmodel`
--

CREATE TABLE `studentexams_subtopicsmodel` (
  `id` int(11) NOT NULL,
  `subTopicName` varchar(200) DEFAULT NULL,
  `status` smallint(6) NOT NULL,
  `course_id_id` int(11) DEFAULT NULL,
  `subject_id_id` int(11) DEFAULT NULL,
  `topic_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studentexams_subtopicsmodel`
--

INSERT INTO `studentexams_subtopicsmodel` (`id`, `subTopicName`, `status`, `course_id_id`, `subject_id_id`, `topic_id_id`) VALUES
(3, 'Thermodynamics', 1, 8, 2, 2),
(4, 'Sub Topics', 1, 9, 3, 3),
(5, 'Metals', 1, 10, 4, 4);

-- --------------------------------------------------------

--
-- Table structure for table `studentexams_topicsmodel`
--

CREATE TABLE `studentexams_topicsmodel` (
  `id` int(11) NOT NULL,
  `topicName` varchar(200) DEFAULT NULL,
  `status` smallint(6) NOT NULL,
  `course_id_id` int(11) DEFAULT NULL,
  `subject_id_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studentexams_topicsmodel`
--

INSERT INTO `studentexams_topicsmodel` (`id`, `topicName`, `status`, `course_id_id`, `subject_id_id`) VALUES
(2, 'Thermodynamics', 1, 8, 2),
(3, 'Topics', 1, 9, 3),
(4, 'Topics', 1, 10, 4);

-- --------------------------------------------------------

--
-- Table structure for table `studentexams_userregistrationmodel`
--

CREATE TABLE `studentexams_userregistrationmodel` (
  `id` int(11) NOT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `mobile` varchar(30) DEFAULT NULL,
  `createdDate` datetime(6) NOT NULL,
  `deletedDate` datetime(6) NOT NULL,
  `updatedDate` datetime(6) NOT NULL,
  `loginDateTime` datetime(6) NOT NULL,
  `logoutDateTime` datetime(6) NOT NULL,
  `status` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studentexams_userregistrationmodel`
--

INSERT INTO `studentexams_userregistrationmodel` (`id`, `firstname`, `lastname`, `username`, `email`, `password`, `mobile`, `createdDate`, `deletedDate`, `updatedDate`, `loginDateTime`, `logoutDateTime`, `status`) VALUES
(4, 'Karishma', 'Soni', 'Karishma123', 'karishma.sony.ks@gmail.com', 'soni@123', '9856896598', '2021-02-02 06:45:08.304753', '2021-02-02 06:45:08.304753', '2021-02-02 06:45:08.304753', '2021-02-02 06:45:08.304753', '2021-02-02 06:45:08.304753', 1),
(5, 'Akhilesh', 'Soni', 'Akhil143', 'akkirads54321@gmail.com', '123456', '9865232154', '2021-02-02 07:08:37.200157', '2021-02-02 07:08:37.200157', '2021-02-02 07:08:37.200157', '2021-02-02 07:08:37.200157', '2021-02-02 07:08:37.200157', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `imagequestionsmodel`
--
ALTER TABLE `imagequestionsmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `imageQuestionsModel_topic_id_id_10be5e91_fk_studentex` (`topic_id_id`),
  ADD KEY `imageQuestionsModel_type_id_id_1e0b8745_fk_studentex` (`type_id_id`);

--
-- Indexes for table `studentexams_courseplanmodel`
--
ALTER TABLE `studentexams_courseplanmodel`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `studentexams_coursereferencemodel`
--
ALTER TABLE `studentexams_coursereferencemodel`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `studentexams_coursesmodel`
--
ALTER TABLE `studentexams_coursesmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `studentexams_courses_student_id_id_9906b848_fk_studentex` (`student_id_id`);

--
-- Indexes for table `studentexams_demouserregistrationmodel`
--
ALTER TABLE `studentexams_demouserregistrationmodel`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `studentexams_questionsmodel`
--
ALTER TABLE `studentexams_questionsmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `studentexams_questio_topic_id_id_3c31385c_fk_studentex` (`topic_id_id`),
  ADD KEY `studentexams_questio_subTopic_id_id_7fea8dbf_fk_studentex` (`subTopic_id_id`),
  ADD KEY `studentexams_questio_type_id_id_56b2acda_fk_studentex` (`type_id_id`);

--
-- Indexes for table `studentexams_questiontypesmodel`
--
ALTER TABLE `studentexams_questiontypesmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `studentexams_questio_topics_id_id_7c4b2939_fk_studentex` (`topics_id_id`);

--
-- Indexes for table `studentexams_studentresultmodel`
--
ALTER TABLE `studentexams_studentresultmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `studentexams_student_student_id_id_d9914807_fk_studentex` (`student_id_id`),
  ADD KEY `studentexams_student_subject_id_id_3ba925b0_fk_studentex` (`subject_id_id`);

--
-- Indexes for table `studentexams_subjectsmodel`
--
ALTER TABLE `studentexams_subjectsmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `studentexams_subject_course_id_id_30d1e7a5_fk_studentex` (`course_id_id`);

--
-- Indexes for table `studentexams_subscriptiondetailsmodel`
--
ALTER TABLE `studentexams_subscriptiondetailsmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `studentexams_subscri_courseType_id_cfceeec5_fk_studentex` (`courseType_id`),
  ADD KEY `studentexams_subscri_userId_id_18009822_fk_studentex` (`userId_id`);

--
-- Indexes for table `studentexams_subscriptionmodel`
--
ALTER TABLE `studentexams_subscriptionmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `studentexams_subscri_courseType_id_d78d51ad_fk_studentex` (`courseType_id`),
  ADD KEY `studentexams_subscri_userId_id_bcef7f38_fk_studentex` (`userId_id`);

--
-- Indexes for table `studentexams_subtopicsmodel`
--
ALTER TABLE `studentexams_subtopicsmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `studentexams_subtopi_course_id_id_506d6933_fk_studentex` (`course_id_id`),
  ADD KEY `studentexams_subtopi_subject_id_id_f5c9aba9_fk_studentex` (`subject_id_id`),
  ADD KEY `studentexams_subtopi_topic_id_id_afc0a5ac_fk_studentex` (`topic_id_id`);

--
-- Indexes for table `studentexams_topicsmodel`
--
ALTER TABLE `studentexams_topicsmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `studentexams_topicsm_course_id_id_f5a5d86f_fk_studentex` (`course_id_id`),
  ADD KEY `studentexams_topicsm_subject_id_id_2f8c24e2_fk_studentex` (`subject_id_id`);

--
-- Indexes for table `studentexams_userregistrationmodel`
--
ALTER TABLE `studentexams_userregistrationmodel`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `imagequestionsmodel`
--
ALTER TABLE `imagequestionsmodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `studentexams_courseplanmodel`
--
ALTER TABLE `studentexams_courseplanmodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `studentexams_coursereferencemodel`
--
ALTER TABLE `studentexams_coursereferencemodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `studentexams_coursesmodel`
--
ALTER TABLE `studentexams_coursesmodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `studentexams_demouserregistrationmodel`
--
ALTER TABLE `studentexams_demouserregistrationmodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `studentexams_questionsmodel`
--
ALTER TABLE `studentexams_questionsmodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `studentexams_questiontypesmodel`
--
ALTER TABLE `studentexams_questiontypesmodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `studentexams_studentresultmodel`
--
ALTER TABLE `studentexams_studentresultmodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `studentexams_subjectsmodel`
--
ALTER TABLE `studentexams_subjectsmodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `studentexams_subscriptiondetailsmodel`
--
ALTER TABLE `studentexams_subscriptiondetailsmodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `studentexams_subscriptionmodel`
--
ALTER TABLE `studentexams_subscriptionmodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `studentexams_subtopicsmodel`
--
ALTER TABLE `studentexams_subtopicsmodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `studentexams_topicsmodel`
--
ALTER TABLE `studentexams_topicsmodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `studentexams_userregistrationmodel`
--
ALTER TABLE `studentexams_userregistrationmodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `imagequestionsmodel`
--
ALTER TABLE `imagequestionsmodel`
  ADD CONSTRAINT `imageQuestionsModel_topic_id_id_10be5e91_fk_studentex` FOREIGN KEY (`topic_id_id`) REFERENCES `studentexams_topicsmodel` (`id`),
  ADD CONSTRAINT `imageQuestionsModel_type_id_id_1e0b8745_fk_studentex` FOREIGN KEY (`type_id_id`) REFERENCES `studentexams_questiontypesmodel` (`id`);

--
-- Constraints for table `studentexams_coursesmodel`
--
ALTER TABLE `studentexams_coursesmodel`
  ADD CONSTRAINT `studentexams_courses_student_id_id_9906b848_fk_studentex` FOREIGN KEY (`student_id_id`) REFERENCES `studentexams_userregistrationmodel` (`id`);

--
-- Constraints for table `studentexams_questionsmodel`
--
ALTER TABLE `studentexams_questionsmodel`
  ADD CONSTRAINT `studentexams_questio_subTopic_id_id_7fea8dbf_fk_studentex` FOREIGN KEY (`subTopic_id_id`) REFERENCES `studentexams_subtopicsmodel` (`id`),
  ADD CONSTRAINT `studentexams_questio_topic_id_id_3c31385c_fk_studentex` FOREIGN KEY (`topic_id_id`) REFERENCES `studentexams_topicsmodel` (`id`),
  ADD CONSTRAINT `studentexams_questio_type_id_id_56b2acda_fk_studentex` FOREIGN KEY (`type_id_id`) REFERENCES `studentexams_questiontypesmodel` (`id`);

--
-- Constraints for table `studentexams_questiontypesmodel`
--
ALTER TABLE `studentexams_questiontypesmodel`
  ADD CONSTRAINT `studentexams_questio_topics_id_id_7c4b2939_fk_studentex` FOREIGN KEY (`topics_id_id`) REFERENCES `studentexams_topicsmodel` (`id`);

--
-- Constraints for table `studentexams_studentresultmodel`
--
ALTER TABLE `studentexams_studentresultmodel`
  ADD CONSTRAINT `studentexams_student_student_id_id_d9914807_fk_studentex` FOREIGN KEY (`student_id_id`) REFERENCES `studentexams_userregistrationmodel` (`id`),
  ADD CONSTRAINT `studentexams_student_subject_id_id_3ba925b0_fk_studentex` FOREIGN KEY (`subject_id_id`) REFERENCES `studentexams_subjectsmodel` (`id`);

--
-- Constraints for table `studentexams_subjectsmodel`
--
ALTER TABLE `studentexams_subjectsmodel`
  ADD CONSTRAINT `studentexams_subject_course_id_id_30d1e7a5_fk_studentex` FOREIGN KEY (`course_id_id`) REFERENCES `studentexams_coursesmodel` (`id`);

--
-- Constraints for table `studentexams_subscriptiondetailsmodel`
--
ALTER TABLE `studentexams_subscriptiondetailsmodel`
  ADD CONSTRAINT `studentexams_subscri_courseType_id_cfceeec5_fk_studentex` FOREIGN KEY (`courseType_id`) REFERENCES `studentexams_coursereferencemodel` (`id`),
  ADD CONSTRAINT `studentexams_subscri_userId_id_18009822_fk_studentex` FOREIGN KEY (`userId_id`) REFERENCES `studentexams_userregistrationmodel` (`id`);

--
-- Constraints for table `studentexams_subscriptionmodel`
--
ALTER TABLE `studentexams_subscriptionmodel`
  ADD CONSTRAINT `studentexams_subscri_courseType_id_d78d51ad_fk_studentex` FOREIGN KEY (`courseType_id`) REFERENCES `studentexams_coursereferencemodel` (`id`),
  ADD CONSTRAINT `studentexams_subscri_userId_id_bcef7f38_fk_studentex` FOREIGN KEY (`userId_id`) REFERENCES `studentexams_userregistrationmodel` (`id`);

--
-- Constraints for table `studentexams_subtopicsmodel`
--
ALTER TABLE `studentexams_subtopicsmodel`
  ADD CONSTRAINT `studentexams_subtopi_course_id_id_506d6933_fk_studentex` FOREIGN KEY (`course_id_id`) REFERENCES `studentexams_coursesmodel` (`id`),
  ADD CONSTRAINT `studentexams_subtopi_subject_id_id_f5c9aba9_fk_studentex` FOREIGN KEY (`subject_id_id`) REFERENCES `studentexams_subjectsmodel` (`id`),
  ADD CONSTRAINT `studentexams_subtopi_topic_id_id_afc0a5ac_fk_studentex` FOREIGN KEY (`topic_id_id`) REFERENCES `studentexams_topicsmodel` (`id`);

--
-- Constraints for table `studentexams_topicsmodel`
--
ALTER TABLE `studentexams_topicsmodel`
  ADD CONSTRAINT `studentexams_topicsm_course_id_id_f5a5d86f_fk_studentex` FOREIGN KEY (`course_id_id`) REFERENCES `studentexams_coursesmodel` (`id`),
  ADD CONSTRAINT `studentexams_topicsm_subject_id_id_2f8c24e2_fk_studentex` FOREIGN KEY (`subject_id_id`) REFERENCES `studentexams_subjectsmodel` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
