add_library( day06 day06.cpp)

target_include_directories(day06 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day06 TBB::tbb )