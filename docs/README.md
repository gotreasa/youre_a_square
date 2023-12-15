# Youre_a_Square

[![License: AGPL](https://img.shields.io/badge/License-AGPL-blue.svg)](https://github.com/gotreasa/youre_a_square/blob/main/LICENSE)
[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=gotreasa_youre_a_square&metric=alert_status)](https://sonarcloud.io/dashboard?id=gotreasa_youre_a_square)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=gotreasa_youre_a_square&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=gotreasa_youre_a_square)
[![Build Status](https://github.com/gotreasa/youre_a_square/actions/workflows/cicd.yml/badge.svg)](https://github.com/gotreasa/youre_a_square/actions/workflows/cicd.yml)
[![Can I Deploy main to test](https://gotreasa.pactflow.io/pacticipants/youre_a_square_app/branches/main/latest-version/can-i-deploy/to-environment/test/badge)](https://gotreasa.pactflow.io/hal-browser/browser.html#https://gotreasa.pactflow.io/pacticipants/youre_a_square_app/branches/main/latest-version/can-i-deploy/to-environment/test/badge)

Welcome to the Python Template created via a cookiecutter recipe. The project template is designed for a development via a `Double Loop approach` (BDD-TDD) using pytest and several other pytest libs.

## Description

### A square of squares

You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

### Task

Given an integral number, determine if it's a square number:

> _In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself._

The tests will always use some integral number, so don't worry about that in dynamic typed languages.

### Examples

```
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
```
