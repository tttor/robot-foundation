# cmake

## print-out-all-accessible-variables-in-a-script
https://stackoverflow.com/questions/9298278/cmake-print-out-all-accessible-variables-in-a-script
```
get_cmake_property(_variableNames VARIABLES)
foreach (_variableName ${_variableNames})
  message(STATUS "${_variableName}=${${_variableName}}")
endforeach()
```
## pass-git-sha1-to-compiler-as-definition-using-cmake
https://stackoverflow.com/questions/1435953/how-can-i-pass-git-sha1-to-compiler-as-definition-using-cmake
```
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake/")
include(GetGitRevisionDescription)
get_git_head_revision(GIT_REFSPEC GIT_SHA1)
configure_file("${CMAKE_CURRENT_SOURCE_DIR}/src/GitSHA1.cpp.in" "${CMAKE_CURRENT_BINARY_DIR}/GitSHA1.cpp" @ONLY)
list(APPEND SOURCES "${CMAKE_CURRENT_BINARY_DIR}/GitSHA1.cpp" GitSHA1.h)
```
