add_library( day10 day10.cpp)

target_include_directories(day10 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day10 TBB::tbb )