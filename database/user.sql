-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 08, 2023 at 01:27 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `user`
--

-- --------------------------------------------------------

--
-- Table structure for table `math_fun`
--

CREATE TABLE `math_fun` (
  `t_no` int(11) NOT NULL,
  `t_name` varchar(20) NOT NULL,
  `t_brief` varchar(1000) DEFAULT NULL,
  `eg_prob` varchar(1000) DEFAULT NULL,
  `soln` varchar(100) DEFAULT NULL,
  `application` varchar(50) DEFAULT NULL,
  `app_brief` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `math_fun`
--

INSERT INTO `math_fun` (`t_no`, `t_name`, `t_brief`, `eg_prob`, `soln`, `application`, `app_brief`) VALUES
(1, 'Angle of Elevation', 'Angle of Elevation(Theta):\nThe angle formed between the horizontal line and the line of sight when an observer is\nlooking up at an object.\nFormulas:\ntan(Theta)= apposite side /adjacent side\nIn the context of angle of elevation, the \"opposite side\" is usually the \nheight of the object being observed, and the \"adjacent side\" is the \nhorizontal distance \r\nfrom the observer to the object.\n\ncos(Theta)=adjacent/hypotenues\nThis is used if you know the horizontal distance and the\n distance along the line of sight.\n\nsin(Theta)=apposite/hypotenuse \nThis is useful if you know the height of the object and the distance along the\n line of sigh\n', 'A tower stands vertically on the ground. From a point on the ground, which is 48m away from the foot of \nthe tower, the angle of elevation of the top of the tower is 30 degree . Find the height of the tower.\n', 'C:\\Users\\sindu\\Documents\\python\\math_fun\\soln_img\\angle of elevation.png', 'Construction', 'The angle of elevation is often used in scenarios like surveying land, calculating \nthe height of objects, and in physics for problems involving projectile motion.\n');

-- --------------------------------------------------------

--
-- Table structure for table `user_info`
--

CREATE TABLE `user_info` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(30) NOT NULL,
  `password` varchar(20) NOT NULL,
  `class` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_info`
--

INSERT INTO `user_info` (`id`, `name`, `password`, `class`) VALUES
(0, 'yuvaraj', 'naruto', 12);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `math_fun`
--
ALTER TABLE `math_fun`
  ADD PRIMARY KEY (`t_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `math_fun`
--
ALTER TABLE `math_fun`
  MODIFY `t_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
