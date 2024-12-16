add_library( day23 day23.cpp)

target_include_directories(day23 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day23 TBB::tbb )