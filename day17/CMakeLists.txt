add_library( day17 day17.cpp)

target_include_directories(day17 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day17 TBB::tbb )