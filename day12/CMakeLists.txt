add_library( day12 day12.cpp)

target_include_directories(day12 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day12 TBB::tbb )